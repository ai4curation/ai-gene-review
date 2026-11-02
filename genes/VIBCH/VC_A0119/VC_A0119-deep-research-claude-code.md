---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:31:30.596360'
end_time: '2026-10-30T21:36:54.626891'
duration_seconds: 324.03
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_A0119
  gene_symbol: VC_A0119
  uniprot_accession: Q9KN46
  protein_description: 'RecName: Full=ImpA N-terminal domain-containing protein {ECO:0000259|Pfam:PF06812};'
  gene_info: OrderedLocusNames=VC_A0119 {ECO:0000313|EMBL:AAF96033.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: ImpA_N. (IPR010657); T6SS-assoc_VCA0119. (IPR017739); ImpA_N (PF06812);
    T6SS_VasJ (PF16989)
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
  web_search_requests: 4
  num_turns: 18
  total_cost_usd: 2.08954752
  session_id: d82fa9da-e15d-48c1-b6fb-5d7125db8fe9
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KN46
- **Protein Description:** RecName: Full=ImpA N-terminal domain-containing protein {ECO:0000259|Pfam:PF06812};
- **Gene Information:** OrderedLocusNames=VC_A0119 {ECO:0000313|EMBL:AAF96033.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ImpA_N. (IPR010657); T6SS-assoc_VCA0119. (IPR017739); ImpA_N (PF06812); T6SS_VasJ (PF16989)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_A0119" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_A0119' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_A0119** (gene ID: VC_A0119, UniProt: Q9KN46) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Schneider et al. 2019 is cached locally with full text. I'm pulling the V. cholerae TssA results from it now.

# Research Report: **VC_A0119** (*tssA* / TssA<sub>VC</sub>; UniProt **Q9KN46**) — *Vibrio cholerae* O1 El Tor N16961

---

## 1. Identity verification

| Field | Value | Source |
|---|---|---|
| UniProt accession | **Q9KN46** (TrEMBL, unreviewed; entry v90, 28-JAN-2026) | local `VC_A0119-uniprot.txt` |
| Length / MW | 469 aa / 53,080 Da | UniProt SQ line |
| UniProt protein name | "ImpA N-terminal domain-containing protein" (`ECO:0000259|Pfam:PF06812`) — a **domain-derived placeholder name**, not a curated functional name | UniProt DE |
| Locus | `OrderedLocusNames=VC_A0119`, **chromosome II (the small chromosome / megaplasmid)** of N16961 | UniProt GN, `DR Proteomes; UP000000584; Chromosome II` |
| Domains | **PF06812 ImpA_N** (FT DOMAIN 12–125); **PF16989 T6SS_VasJ** (C-terminal); IPR010657 (ImpA_N), **IPR017739 "T6SS-assoc_VCA0119"**; NCBIfam **TIGR03362 (VI_chp_7)**; PANTHER **PTHR37024:SF3 "TYPE VI SECRETION SYSTEM PROTEIN TSSA"**; eggNOG **COG3515**; TCDB **3.A.23.1.1** (T6SS family) | UniProt DR/FT |
| Experimental structure | **PDB 6RIU**, cryo-EM 3.90 Å, chains A/B = residues 1–469 | UniProt DR; [RCSB 6RIU](https://www.rcsb.org/structure/6riu) |
| Evidence level | **PE 1: Evidence at protein level** | UniProt PE |
| Other features | Disordered region 185–214 (MobiDB-lite), low-complexity 200–210 | UniProt FT |

**Verification outcome: the identification is unambiguous and confirmed by primary literature.** The target protein is explicitly and repeatedly named in Schneider *et al.* (2019, *EMBO J*), which states that Class A of TssA-like proteins "is represented by *E. coli* TssA<sub>EC</sub> (EC042_4540) and *A. hydrophila* TssA<sub>AH</sub> (AHA1844), as well as **V. cholerae TssA<sub>VC</sub> (VCA0119)**", and whose Methods record that "*tssA*<sub>VC</sub> (amino acids 1–469, **Gene number: VC_A0119**) of *V. cholerae* VC2740-80 was cloned into a modified pACEBACI expression [vector]". The 469-aa length, the ImpA_N + VasJ architecture, the chromosome-II *vas* locus position, and PDB 6RIU all agree. There is **no gene-symbol ambiguity problem** here: the protein is the *V. cholerae* **TssA**, the only Class A TssA-like protein of this organism's single T6SS, and it is distinct from the paralogous ImpA_N protein **TagA<sub>VC</sub>** discussed below.

One important caveat for annotation: **the local `VC_A0119-goa.tsv` is empty — this protein currently carries zero GO annotations** despite having a published cryo-EM structure, a defined mutant phenotype, and a named mechanistic role. That is a substantial curation gap, not a knowledge gap.

Note also the naming churn in the literature: the same protein appears as **VCA0119**, **VC_A0119**, **TssA<sub>VC</sub>**, historically **VasJ** (the C-terminal Pfam domain PF16989 is named for the *vas* gene nomenclature), and Schneider *et al.* propose renaming its whole class to **TsaC** (T6SS sheath assembly chaperone). All refer to Q9KN46.

---

## 2. Biological context: the *V. cholerae* type VI secretion system

The T6SS is a membrane-anchored contractile nanomachine, structurally and functionally homologous to the contractile tail of bacteriophages and R-type pyocins, that injects proteins from the bacterial cytosol directly into an extracellular space or across a target-cell membrane ([Schneider *et al.* 2019, *EMBO J* 38:e100825](https://doi.org/10.15252/embj.2018100825), PMID:31403721, Introduction). Its biogenesis proceeds in a strictly hierarchical order: a trans-envelope **membrane complex** (TssJLM) forms first; the **baseplate** (VgrG, TssE, TssF, TssG, TssK) assembles on it; then the **sheath–tube** copolymer (TssB/VipA + TssC/VipB sheath around an Hcp tube) polymerizes from the baseplate across the cytoplasm. Once fully extended, the sheath contracts rapidly, propelling the inner tube and its associated effectors out of the cell; the contracted sheath is then disassembled by the AAA+ unfoldase **ClpV** and its subunits recycled (same reference, with the primary citations therein: Basler *et al.* 2012; Bönemann *et al.* 2009; Brunet *et al.* 2015; Nguyen *et al.* 2017; Nazarov *et al.* 2018).

In *V. cholerae*, this machine is both **anti-eukaryotic** (virulence toward *Dictyostelium discoideum* amoebae) and **anti-bacterial** (contact-dependent killing of competitor cells such as *E. coli*). The systematic single-gene mutagenesis of the *V. cholerae* V52 T6SS locus by [Zheng, Ho & Mekalanos (2011) *PLoS ONE* 6:e23876](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3166118/) scored every locus gene for Hcp expression, Hcp secretion, amoeba virulence, and *E. coli* killing. Deletion of 15 individual genes abolished amoeba virulence; **twelve of these — including VCA0119 — were required for secretion of Hcp but not for its expression**, the signature of a structural/assembly component rather than a regulator or effector. (By contrast, VasH and VCA0122 behaved as expression regulators, and VCA0118 as a candidate effector.) This is the earliest genetic placement of VC_A0119 inside the secretion apparatus itself.

---

## 3. Primary molecular function: a sheath-assembly chaperone / processivity cap at the distal end of the growing sheath

VC_A0119 is **not an enzyme, not a transporter, and not a secreted effector**. It is a **cytoplasmic, self-assembling oligomeric scaffold protein** that caps the growing tip of the T6SS sheath–tube polymer and catalyses its elongation. The mechanistic case rests on four independent lines of evidence in Schneider *et al.* (2019), all obtained in *V. cholerae* itself.

### 3.1 Loss-of-function phenotype: sheath elongation collapses

Live-cell fluorescence imaging of VipA-mCherry2-labelled sheaths showed that the parental strain forms ~5 T6SS structures per cell during logarithmic growth, whereas "the *tssA*<sub>VC</sub>-negative strain formed mostly dynamic sheath spots and only few structures that fully extended and contracted." Quantitatively, **sheath polymerization speed dropped from 23 nm/s in the parent to 3 nm/s in the Δ*tssA*<sub>VC</sub> strain** — an ~8-fold loss of elongation rate. In bacterial competition assays the Δ*tssA*<sub>VC</sub> knockout "was able to kill *E. coli* prey cells only at a reduced rate", a defect the authors note "resembled the reduced prey cell killing by a strain lacking the baseplate component *tssE*."

Crucially, the defect is **kinetic and processivity-related, not all-or-none**: "TssA<sub>VC</sub> is not strictly required for sheath assembly as *tssA*<sub>VC</sub>-negative strain still kills prey cells, assembles short dynamic sheaths and occasionally also full-length sheath with significantly reduced assembly speed." This distinguishes *V. cholerae* TssA from the orthologues in *E. coli* and *P. aeruginosa* H1-T6SS, where Hcp/effector secretion was reported to be undetectable in the knockouts (Zoued *et al.* 2016; Planamente *et al.* 2016, as reviewed in Schneider *et al.* 2019). The *V. cholerae* genetic result of Zheng *et al.* (2011) — VCA0119 required for Hcp secretion — and the imaging result are reconcilable: a system reduced to short, infrequent sheaths loses bulk Hcp secretion in a population assay while retaining residual single-cell firing.

### 3.2 Localization: the distal (membrane-distal) end of the polymerizing sheath

A chromosomal **TssA<sub>VC</sub>-mNeonGreen** fusion (functional, though it slowed polymerization to 11 nm/s) was imaged in a VipA-mCherry2 sheath background. "In most cases, TssA<sub>VC</sub> **first localized to T6SS assembly initiation site before sheath signal appeared** and then colocalized with a **distal end of a polymerizing sheath**" — i.e. it is recruited at the baseplate/membrane-proximal initiation site, then travels at the advancing tip, remaining at the end farthest from the membrane anchor. Kymograph analysis of 300 cells partitioned the behaviour: in ~two-thirds of events TssA<sub>VC</sub> stayed attached until contraction (<5 s after full assembly); in ~27% it dissociated after the sheath reached the opposite membrane, which was followed by a prolonged stably extended sheath; in ~3% it remained attached even after contraction. Dissociation and re-association events were also seen, with the authors describing re-association as allowing TssA<sub>VC</sub> "to continue catalysis of polymerization."

**Subcellular location is therefore cytoplasmic**, at a dynamic, sub-diffraction-sized site on the inner face of the cell envelope and then along the cytoplasmic path of the extending sheath. It is not an integral membrane protein (no transmembrane segments in the UniProt record), and it is not itself secreted — unlike Hcp or VgrG it is a machine component that stays inside.

### 3.3 The cap is a stable, non-exchanging dodecamer

Two orthogonal measurements establish the oligomeric state **in vivo**:

- **Photobleaching.** Cytosolic TssA<sub>VC</sub>-mNeonGreen was photobleached during sheath polymerization; "TssA<sub>VC</sub>-mNeonGreen signal of the complex at the distal end of the polymerizing sheath remained constant after photobleaching of the cytosol, suggesting that the TssA<sub>VC</sub> subunits are **not exchanged with the cytosolic TssA<sub>VC</sub> pool** during sheath polymerization." The cap is thus assembled once and rides the tip as a unit — a *processive* cap, not a transiently sampling factor.
- **Single-molecule step calibration.** Spot intensities were compared against a LacI-mNeonGreen/*lacO*-array standard (0, 3, 6, 12 operators). "Signals observed for TssA<sub>VC</sub>-mNeonGreen fusions were most similar to the signal produced by LacI-mNeonGreen molecules binding to 6 copies of *lacO*… This suggests that **TssA<sub>VC</sub> forms a dodecamer in vivo**."

### 3.4 Cryo-EM structure (PDB 6RIU / this study): a 12-subunit two-ring star that matches the sheath tip

Recombinant full-length TssA<sub>VC</sub> (1–469, expressed in insect cells via MultiBac) was purified and solved by cryo-EM. Key structural findings:

- **Symmetry and dimensions.** Unbiased C1 refinement "resulted in clear **six-pointed star** reconstruction"; refinement then used C6. "The **outer and lumenal diameters are 132 and 53 Å, and the height of the assembly is 38 Å.**"
- **Stoichiometry confirmed biochemically.** "Molecular weight estimation from the size-exclusion chromatography (SEC) profile is ~600 kDa, which corresponds to **twelve copies of TssA<sub>VC</sub>** in one oligomer (634 kDa from sequence)."
- **The ordered core is the C-terminal VasJ domain.** "The model built in cryo-EM density of TssA<sub>VC</sub> is composed of **twelve C-terminal subunits (G376–T466, helices α8–α12) tightly packed as two interpenetrating rings**", resolved to a **global resolution of 3.9 Å** (consistent with PDB 6RIU's deposited 3.90 Å). This parallels the *E. coli* TssA<sub>EC</sub> C-terminal VasJ-domain crystal structure, which forms "two stacked hexameric rings" (Zoued *et al.* 2016).
- **A flexible middle domain decorates the ring.** "Well-resolved TssA<sub>VC</sub> star-like CTD is surrounded by disordered density… which most likely represents the middle N-terminal domain (**Nt2**)", resolved as **Nt2 dimers** (six per particle) after symmetry expansion and focused classification to 6.6–10 Å, with a modelled range of motion of roughly ±60° relative to the CTD ring plane. The MobiDB-lite disordered region at 185–214 in the UniProt record corresponds to the kind of flexible linker that permits this.
- **Direct structural identification of the sheath-tip cap.** "Our reconstruction of TssA<sub>VC</sub> CTD **fits as a rigid body with CC = 0.87 into the distal end of VipA-N3 sheath mutant reconstruction** (EMD-3878)." This is the decisive structural link: the sixfold "flattened star-like complex" at the distal end of isolated non-contractile *V. cholerae* sheaths — which [Nazarov *et al.* 2018, *EMBO J*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5813253) reported at 7.5 Å (EMD-3878) but could not assign compositionally, noting only that it "could be either VipA/VipB sheath subunits without the Hcp ring or a cap" — **is TssA<sub>VC</sub>**.

The dodecameric ring's dimensions are, as noted for the homologous TssA1<sub>PA</sub>, "similar to sheath-tube ring" with "a central hole that could accommodate Hcp" — geometrically consistent with a template/jig that holds the leading sheath–tube ring in register.

### 3.5 Mechanistic interpretation: a chaperone for sheath–tube copolymerization

Schneider *et al.* reason by comparison with phage T4, whose sheath elongation requires no chaperone (Arisaka *et al.* 1979): "while potentially not being strictly essential, **Class A TssAs act as chaperones assisting sheath-tube copolymerization, which likely requires assistance in proper formation of the sheath hand-shake domain**" — the interdigitating TssB/TssC extension that locks successive sheath rings together (Ge *et al.* 2015; Kudryashev *et al.* 2015; Wang *et al.* 2017). On this basis they propose the class name **TsaC (T6SS sheath assembly chaperone)**. The functional model (their Fig 6A) is: *after the membrane complex forms, TsaC assists in recruitment of baseplate components and sheath–tube copolymerization; once the extending sheath–tube reaches the opposing cell membrane, TsmA (TagA) replaces TsaC at the distal end and holds it in place; shortly after TsmA disappearance the sheath contracts and releases the spike/tube to the environment; sheath components are then recycled by ClpV.*

Domain division of labour is inferred by homology to *E. coli*, where "the **N-terminal part of TssA<sub>EC</sub> containing ImpA_N domain** might be responsible for **interaction with sheath** and to a lesser extent with baseplate components, while the **C-terminus** preferably interacted with **Hcp**" (Zoued *et al.* 2016, as summarized in Schneider *et al.* 2019). The *V. cholerae* protein's architecture (ImpA_N 12–125, flexible Nt2, VasJ CTD ~376–466) is consistent with this partition, but the per-domain binding assignment for Q9KN46 specifically has not been separately mapped — a genuine open question.

---

## 4. Protein–protein interactions and the TagA antagonism

The interaction data reported for *V. cholerae* come from HA-tag co-immunoprecipitation followed by mass spectrometry, plus bacterial two-hybrid assays (Schneider *et al.* 2019, Methods and author contributions). The published summary statement is about the paralogue: "We show that **TagA<sub>VC</sub> interacts with TssA<sub>VC</sub>, TssK, ClpV, VipA, and VipB**" — placing TssA<sub>VC</sub> in a physical network with the baseplate (TssK), the sheath (VipA/TssB, VipB/TssC), the recycling ATPase (ClpV), and TagA. For the orthologues, the reported partner sets are TssK, TssE, VgrG, Hcp, TssB, TssC (TssA<sub>EC</sub>; Zoued *et al.* 2016) and TssK1, TssF1, ClpV1, Hcp1, TssB1 (TssA1<sub>PA</sub>; Planamente *et al.* 2016).

**TagA<sub>VC</sub> is the functional antagonist of VC_A0119**, and the two are the reason *V. cholerae* is the organism where the TssA/TagA relationship was dissected. TagA<sub>VC</sub> (Class B: ImpA_N followed by a hydrophobic domain) "localizes to cell membrane and prevents sheath assembly likely by competing with TssA<sub>VC</sub>", forming hexameric spots at the distal ends of fully assembled sheaths. Three observations tie the two together:

1. TssA<sub>VC</sub> spots normally disappear from fully extended sheaths (their Fig 2C).
2. In the Δ*tagA*<sub>VC</sub> mutant, "the fraction of sheaths with TssA<sub>VC</sub>-mNeonGreen spots still attached to sheath distal end after contraction **increased from 3% in the parental strain to 30%**."
3. Overproducing TagA<sub>VC</sub> blocked sheath assembly entirely and froze TssA<sub>VC</sub>-mNeonGreen spots at the membrane, colocalized with sheath foci: "High concentration of TagA<sub>VC</sub> thus results in **retention of TssA<sub>VC</sub> at sheath assembly initiation sites and inhibition of sheath assembly**." Overproducing TssA<sub>VC</sub> itself had no such effect (killing and sheath assembly remained like the parent).

Interpretation: "**TagA<sub>VC</sub> blocks function of TssA<sub>VC</sub> potentially by removing TssA<sub>VC</sub> from the fully assembled sheath. Removal of TssA<sub>VC</sub> stops or slows down further sheath polymerization and thus stabilizes the extended sheath.**" Phenotypically, Δ*tagA*<sub>VC</sub> gives ~5-fold fewer sheath assemblies, ~3-fold fewer contractions, reduced polymerization speed (13 vs 23 nm/s), and sheaths that are "mostly very long, stretching from one pole of a cell to another", often bent and sometimes detached from the membrane anchor — yet with negligible effect on killing. Schneider *et al.* propose renaming this class **TsmA (T6SS sheath membrane anchor)**.

So the elongation switch in *V. cholerae* is a two-protein, two-ImpA_N-protein module: **TssA<sub>VC</sub> (VC_A0119) licenses and accelerates elongation from the tip; TagA<sub>VC</sub> terminates it at the far membrane.**

---

## 5. Evolutionary and bioinformatic placement

- **PF06812 (ImpA_N) is a shared N-terminal module across functionally divergent proteins.** Schneider *et al.* conclude that "proteins with a conserved N-terminal domain **PF06812** cluster into **three main classes** and mainly differ in their C-terminal sequence", and that "while various proteins share a conserved N-terminal domain, their roles in T6SS biogenesis are **fundamentally different**." This is a direct caution against transferring function on ImpA_N presence alone, and it means UniProt's placeholder name "ImpA N-terminal domain-containing protein" is uninformative about what Q9KN46 does.
  - **Class A (TssA / proposed TsaC)** — ImpA_N + **C-terminal VasJ (PF16989)**: TssA<sub>VC</sub> (VC_A0119), TssA<sub>EC</sub> (EC042_4540), TssA<sub>AH</sub> (AHA1844), TssA2<sub>PA</sub> (PA1656). Distal-end dodecameric cap; accelerates initiation and elongation.
  - **Class B (TagA / proposed TsmA)** — ImpA_N + hydrophobic domain: TagA<sub>VC</sub>, TagA<sub>EC</sub>. Membrane-localized elongation stop/anchor.
  - **Class C (proposed TsaB)** — e.g. TssA1<sub>PA</sub> of the *P. aeruginosa* H1-T6SS: baseplate-localized, required for initiation of sheath assembly.
- **Q9KN46's two-domain architecture (PF06812 + PF16989) places it squarely in Class A**, matching both its Pfam complement in UniProt and its PANTHER subfamily assignment **PTHR37024:SF3 "Type VI secretion system protein TssA"**. The NCBIfam model **TIGR03362 (VI_chp_7)** and the dedicated InterPro entry **IPR017739 "T6SS-associated VCA0119"** are both built around this protein lineage, i.e. the family signatures are effectively defined by it.
- **Orthologue identity is low but the function is conserved**: TssA<sub>VC</sub> shares **19.9%** identity with TssA<sub>EC</sub>, **32.8%** with TssA<sub>AH</sub>, and **21.8%** with TssA2<sub>PA</sub>. Despite that divergence, "TssA2<sub>PA</sub> displays almost identical dynamics to TssA<sub>VC</sub>", leading to the generalization that "it is very likely that **all TssA proteins of the Class A perform the same function** in T6SS biogenesis and are required for fast and efficient polymerization of T6SS sheath." Function in this family is thus carried by the domain architecture and the oligomeric geometry, not by sequence conservation — an important point for homology-based annotation of other Vibrionaceae TssA proteins.
- **Fold/assembly relationships.** The Class A CTD two-interpenetrating-ring architecture is shared with TssA<sub>EC</sub> ("two stacked hexameric rings") and TssA<sub>AH</sub>, whose crystal packing also showed the Nt2-dimer behaviour reproduced in the *V. cholerae* cryo-EM map (Dix *et al.* 2018). TssA1<sub>PA</sub> (Class C) was noted to resemble phage baseplate component **gp6** in its C-terminal part (Planamente *et al.* 2016) — consistent with the T6SS's overall phage-tail ancestry.
- **TCDB 3.A.23.1.1** assigns the protein to the "Type VI symbiosis/virulence secretory system (T6SS)" family — correct at the system level, though the TC framing as a transport system should not be read as implying VC_A0119 is itself a transporter.

---

## 6. Summary of function, location and pathway

**Primary function.** VC_A0119 / Q9KN46 is **TssA of the *Vibrio cholerae* type VI secretion system** — a non-catalytic, self-assembling **dodecameric sheath-assembly chaperone and processivity cap**. It is recruited to the T6SS assembly initiation site at the inner membrane before sheath signal is detectable, then rides the **membrane-distal tip** of the elongating TssB/TssC(VipA/VipB) sheath–Hcp tube copolymer as a stable, non-exchanging 12-subunit star-shaped ring (outer Ø 132 Å, lumen Ø 53 Å, height 38 Å; the ordered core being twelve copies of the C-terminal VasJ domain, residues ~376–466, in two interpenetrating hexameric rings), where it templates and accelerates addition of successive sheath–tube rings — most plausibly by assisting correct formation of the sheath hand-shake interface.

**Location of action.** **Cytoplasm**, at a dynamic membrane-proximal initiation site and then at the advancing cytoplasmic tip of the sheath; a component of the **T6SS sheath–tube complex / distal-end cap**, physically continuous with the baseplate at initiation. It is a machine subunit, not a secreted substrate, and has no transmembrane or signal features.

**Pathway.** The hierarchical T6SS biogenesis/firing cycle: membrane complex (TssJLM) → baseplate (TssE/F/G/K, VgrG) → **TssA-capped sheath–tube elongation (this protein)** → TagA-mediated elongation arrest and distal membrane anchoring → contraction and effector/Hcp expulsion → ClpV-dependent sheath disassembly and subunit recycling. Downstream biological outputs are **contact-dependent interbacterial antagonism** (killing of *E. coli* and other competitors) and **anti-eukaryotic virulence** (toward *D. discoideum*). Loss of VC_A0119 reduces, but does not abolish, both: elongation rate falls from 23 to 3 nm/s, full-length sheaths become rare, and prey killing is slowed to roughly the level of a baseplate (*tssE*) mutant, while bulk Hcp secretion is scored as lost in population assays.

**Evidence quality.** Unusually strong and multi-modal for a 469-aa protein of an unreviewed TrEMBL entry: single-cell live imaging of a functional chromosomal fluorescent fusion (localization, dynamics, polymerization kinetics), FRAP/photobleaching (subunit exchange), single-molecule intensity calibration (stoichiometry in vivo), a 3.9 Å cryo-EM structure of the purified complex with SEC mass corroboration (PDB 6RIU), rigid-body fitting into an independently determined in-situ sheath-end map (EMD-3878, CC = 0.87), co-IP/MS and bacterial two-hybrid interaction mapping, deletion phenotyping, and competition assays — plus independent prior genetic evidence that VCA0119 is required for Hcp secretion but not Hcp expression. The main residual uncertainties are (i) which domain of **this** protein contacts sheath versus Hcp (assigned only by *E. coli* homology), (ii) whether the Nt2 flexibility has a defined mechanical role in ring addition, and (iii) the molecular nature of the TssA→TagA handover at the far membrane.

---

## Sources

- [Schneider JP, Nazarov S, Adaixo R, Liuzzo M, Ringel PD, Stahlberg H, Basler M. "Diverse roles of TssA-like proteins in the assembly of bacterial type VI secretion systems." *EMBO J* 38(18):e100825, 16 Sep 2019 (epub 12 Aug 2019). PMID:31403721; PMC6745524](https://doi.org/10.15252/embj.2018100825) — full text read from the local cache `publications/PMID_31403721.md`; all quoted passages above are verbatim from it. **The primary and definitive source for VC_A0119.**
- [Zheng J, Ho B, Mekalanos JJ. "Genetic Analysis of Anti-Amoebae and Anti-Bacterial Activities of the Type VI Secretion System in *Vibrio cholerae*." *PLoS ONE* 6(8):e23876, 31 Aug 2011. PMC3166118](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3166118/) — VCA0119 required for Hcp secretion but not expression; structural-component classification.
- [Nazarov S *et al.* "Cryo-EM reconstruction of Type VI secretion system baseplate and sheath distal end." *EMBO J* 2018. PMC5813253](https://pmc.ncbi.nlm.nih.gov/articles/PMC5813253) — EMD-3878 (sheath distal end, 7.5 Å) and EMD-3879 (baseplate, 8.0 Å); the unassigned sixfold cap later identified as TssA<sub>VC</sub>.
- [PDB 6RIU — "C-terminal domain of TssA protein from T6SS of *Vibrio cholerae*", cryo-EM 3.90 Å](https://www.rcsb.org/structure/6riu); [PDBj EM Navigator entry for 6RIU](https://pdbj.org/emnavi/quick.php?id=6riu); [Proteopedia 6riu](https://proteopedia.org/w/6riu)
- [EMD-3878 (PDBj EM Navigator)](https://pdbj.org/emnavi/quick.php?id=3878) and [EMD-3879](https://pdbj.org/emnavi/quick.php?id=3879)
- [Schneider JP, doctoral thesis / Basler lab record, University of Basel edoc 71708](https://edoc.unibas.ch/71708/); [Nazarov S, "Mechanistic and structural insights into the type VI secretion system tail of *Vibrio cholerae*", edoc 61043](https://edoc.unibas.ch/61043)
- Local repository files (machine-fetched, not edited): `genes/VIBCH/VC_A0119/VC_A0119-uniprot.txt` (UniProt Q9KN46, entry v90, 28-JAN-2026 — DE/GN/OS/DR/FT/PE/SQ lines quoted above); `genes/VIBCH/VC_A0119/VC_A0119-goa.tsv` (**header only — no GO annotations exist for this protein**).
- Secondary works cited through Schneider *et al.* 2019 and not independently retrieved here: Zoued *et al.* 2016 (TssA<sub>EC</sub>: dodecamer, stacked hexameric rings, interaction set, N- vs C-terminal binding preferences); Planamente *et al.* 2016 (TssA1<sub>PA</sub>: gp6-like CTD, baseplate component, interaction set); Dix *et al.* 2018 (TssA<sub>AH</sub> Nt2-CTD crystal packing); Santin *et al.* 2018 and Szwedziak & Pilhofer 2019 (TagA<sub>EC</sub>: membrane anchoring, excessive polymerization on deletion, non-canonical contractions); Vettiger & Basler 2016 (*tssE* sheath counts; short sheaths still deliver effectors); Nazarov *et al.* 2018; Basler *et al.* 2012; Bönemann *et al.* 2009; Ge *et al.* 2015; Kudryashev *et al.* 2015; Wang *et al.* 2017; Arisaka *et al.* 1979.

## Citations

1. https://www.rcsb.org/structure/6riu
2. https://doi.org/10.15252/embj.2018100825
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3166118/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC5813253
5. https://pdbj.org/emnavi/quick.php?id=6riu
6. https://proteopedia.org/w/6riu
7. https://pdbj.org/emnavi/quick.php?id=3878
8. https://pdbj.org/emnavi/quick.php?id=3879
9. https://edoc.unibas.ch/71708/
10. https://edoc.unibas.ch/61043