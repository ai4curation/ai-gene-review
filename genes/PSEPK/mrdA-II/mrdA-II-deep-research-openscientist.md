---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T22:58:12.165530'
end_time: '2026-08-31T23:52:41.413434'
duration_seconds: 3269.25
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mrdA-II
  gene_symbol: mrdA-II
  uniprot_accession: Q88DL8
  protein_description: 'RecName: Full=Peptidoglycan D,D-transpeptidase MrdA {ECO:0000256|HAMAP-Rule:MF_02081};
    EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02081}; AltName: Full=Penicillin-binding
    protein 2 {ECO:0000256|HAMAP-Rule:MF_02081}; Short=PBP-2 {ECO:0000256|HAMAP-Rule:MF_02081};'
  gene_info: Name=mrdA-II {ECO:0000313|EMBL:AAN70376.1}; Synonyms=mrdA {ECO:0000256|HAMAP-Rule:MF_02081};
    OrderedLocusNames=PP_4807 {ECO:0000313|EMBL:AAN70376.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the transpeptidase family. MrdA subfamily.
  protein_domains: Beta-lactam/transpept. (IPR050515); Beta-lactam/transpept-like.
    (IPR012338); PBP_dimer. (IPR005311); PBP_dimer_sf. (IPR036138); PCN-bd_Tpept.
    (IPR001460)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mrdA-II-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mrdA-II-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88DL8
- **Protein Description:** RecName: Full=Peptidoglycan D,D-transpeptidase MrdA {ECO:0000256|HAMAP-Rule:MF_02081}; EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02081}; AltName: Full=Penicillin-binding protein 2 {ECO:0000256|HAMAP-Rule:MF_02081}; Short=PBP-2 {ECO:0000256|HAMAP-Rule:MF_02081};
- **Gene Information:** Name=mrdA-II {ECO:0000313|EMBL:AAN70376.1}; Synonyms=mrdA {ECO:0000256|HAMAP-Rule:MF_02081}; OrderedLocusNames=PP_4807 {ECO:0000313|EMBL:AAN70376.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the transpeptidase family. MrdA subfamily.
- **Key Domains:** Beta-lactam/transpept. (IPR050515); Beta-lactam/transpept-like. (IPR012338); PBP_dimer. (IPR005311); PBP_dimer_sf. (IPR036138); PCN-bd_Tpept. (IPR001460)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mrdA-II" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mrdA-II' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mrdA-II** (gene ID: mrdA-II, UniProt: Q88DL8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *mrdA-II* (PBP-2) in *Pseudomonas putida* KT2440

**Gene:** `mrdA-II` (synonym `mrdA`; ordered locus **PP_4807**)
**Protein:** Peptidoglycan D,D-transpeptidase MrdA / Penicillin-binding protein 2 (PBP-2)
**UniProt:** Q88DL8 · **EC:** 3.4.16.4
**Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125), a Gram-negative, rod-shaped soil γ-proteobacterium
**Family:** Transpeptidase family, MrdA subfamily (Class B high-molecular-mass PBP)
**Signature domains:** Penicillin-binding, transpeptidase (IPR001460); Beta-lactam/transpeptidase-like (IPR012338, IPR050515); PBP dimerization "pedestal" domain (IPR005311, IPR036138)

---

## 1. Identity verification

The gene symbol, the UniProt description, the assigned EC number (3.4.16.4, serine-type D-Ala-D-Ala transpeptidase/carboxypeptidase activity), and the InterPro domain complement are **mutually consistent** and unambiguously identify Q88DL8 as a **Class B penicillin-binding protein 2 (PBP2/MrdA)**. The PCN-bd_Tpept (IPR001460) transpeptidase domain plus the PBP_dimer "pedestal" domain (IPR005311/IPR036138) is the diagnostic two-module architecture of the MrdA/PBP2 subfamily. No conflicting gene-symbol ambiguity was encountered.

**One organism-specific point, established here directly:** the symbol is `mrdA-**II**` because *P. putida* KT2440 encodes **two** paralogous PBP2/MrdA transpeptidases. A UniProt proteome query (taxid 160488) returns **mrdA-I = PP_3741** (Q88GI2, 631 aa) and **mrdA-II = PP_4807** (Q88DL8, 629 aa; the target), alongside the divisome transpeptidase **FtsI/PBP3** (PP_1331) and the bifunctional class A PBPs **PBP1A** (*mrcA*/PP_5084) and **PBP1B** (*mrcB*/PP_4683). A BLOSUM62 global alignment shows the two PBP2 paralogs are **70.8% identical** (464/655 aligned positions) — high similarity but clearly distinct, indicating a retained, functional gene duplication rather than a recent identical copy or a pseudogene.

**Importantly, despite the "-II" suffix, the target PP_4807 is the *genomically canonical* elongation PBP2.** Its gene sits in the classic **mrd operon**: the immediately upstream gene **PP_4806 = *mrdB/rodA*** (Q88DL9) encodes the SEDS **peptidoglycan glycosyltransferase RodA** (EC 2.4.99.28) — the obligate partner of PBP2 in the elongasome — with **PP_4805 = *mltB*** (a lytic transglycosylase) just beyond it. This *mrdA–mrdB(rodA)* tandem mirrors the *E. coli mrdAB* operon. The paralog *mrdA-I* (PP_3741), by contrast, is **not** in an *mrd* operon (its neighbours are a major-facilitator transporter, a porin-like protein and a glutathione S-transferase, with no adjacent *rodA*), marking it as the divergent, orphan/accessory copy. Thus **mrdA-II is the PBP2 physically coupled to its cognate RodA**, and the functional description below applies to it with organism-specific genomic support. Direct wet-lab enzymology of PP_4807 in isolation is not yet published, so cross-organism family biochemistry/structure supplies mechanistic detail; the diagnostic catalytic features are nonetheless confirmed **directly on the Q88DL8 sequence** (§2).

---

## 2. Primary molecular function — the catalyzed reaction and substrate specificity

MrdA/PBP2 is a **serine D,D-transpeptidase** that catalyzes the **crosslinking step of peptidoglycan (PG, murein) synthesis**. "Penicillin-binding protein 2 (PBP2) plays a key role in the formation of peptidoglycans in bacterial cell walls by crosslinking glycan chains through transpeptidase activity" (Choi et al. 2024, PMID 38581948).

- **Reaction:** a D,D-transpeptidation. The enzyme's active-site serine attacks the terminal **D-Ala–D-Ala** peptide bond of a donor stem peptide, forming an acyl-enzyme intermediate and releasing the terminal D-Ala. The acyl group is then transferred to the free amino group of the **meso-diaminopimelate (mDAP)** residue at position 3 of an acceptor stem peptide on a neighbouring glycan strand, producing a **4→3 (D-Ala–mDAP) crosslink**. In Gram-negative γ-proteobacteria such as *P. putida* the acceptor is mDAP, giving the canonical A1γ (DAP-type) murein.
- **Substrate:** the peptide side-chains of nascent **Lipid II–derived glycan strands** (GlcNAc-MurNAc backbone bearing the pentapeptide L-Ala–D-Glu–mDAP–D-Ala–D-Ala). The natural substrate is therefore the polymerized, membrane-associated glycan, not free Lipid II.
- **Structure–function basis:** crystal structures of family members show "an elongated two-domain structure, consisting of a transpeptidase domain and a pedestal domain, and … typical active site residues necessary for transpeptidase activity, as observed in other PBP2 proteins" (Choi et al. 2024, PMID 38581948). The transpeptidase domain carries the conserved SxxK, S/YxN and K(T/S)G catalytic motifs; the SxxK serine is the nucleophile.
- **Confirmed directly on Q88DL8 (this study, sequence analysis):** the 629-aa target protein contains, in the correct order and spacing, all diagnostic elements: an N-terminal cytoplasmic tail (res 1–20) → single transmembrane helix (res 21–41) → pedestal/dimerization domain (res 63–236, Pfam PF03717) → transpeptidase domain (res 268–604, Pfam PF00905), with the **SxxK nucleophile motif S327-T-I-K330** (UniProt annotates Ser327 as the acyl-ester intermediate) and the **K[S/T]G motif G537-K-S-G540** that lines the substrate/β-lactam pocket. InterPro assigns the subfamily-specific signature **IPR017790 "Penicillin-binding protein 2."** These features are present in the actual sequence, so Ser327 is the predicted catalytic nucleophile of *this* enzyme.
- **Pharmacological signature (mechanistic evidence of function):** because the catalytic serine mimics the D-Ala–D-Ala substrate, **β-lactam antibiotics acylate and irreversibly inhibit it** — this is the "penicillin-binding" property. PBP2 is the specific target of the amidinopenicillin **mecillinam (amdinocillin)**: "amdinocillin (mecillinam) show[s] selectivity for PBP2" (Kocaoglu & Carlson 2015, PMID 25733506), and "the beta-lactam mecillinam specifically targets the PBP2 enzyme in the cell elongation machinery of *Escherichia coli*" (Lai et al. 2017, PMID 28749938). In pseudomonads specifically, PBP2 is the antibacterial target of the diazabicyclooctane "β-lactam enhancers" zidebactam/WCK 5153 (Moya et al. 2017, PMID 28289035), and a PBP2 point mutation (V516M) confers zidebactam resistance in *Pseudomonas* (Sastre-Femenia et al. 2026, PMID 42294650) — direct evidence that PBP2 is the physiological, drug-relevant transpeptidase in this genus.

---

## 3. Biological process — cell elongation via the Rod complex (elongasome)

MrdA/PBP2 is the **cognate transpeptidase of the cell-elongation ("Rod") peptidoglycan synthase**, working in an obligate partnership with the SEDS-family glycosyltransferase **RodA**:

- **RodA–PBP2 is a two-enzyme PG synthase.** A SEDS glycosyltransferase and a Class B PBP "form the core of the multi-protein complex required for PG assembly" (Nygaard et al. 2023, PMID 37620344, cryo-EM of the *E. coli* RodA–PBP2 complex). RodA polymerizes Lipid II into a nascent glycan strand; the strand is then delivered to the PBP2 transpeptidase site for crosslinking into the existing sacculus, "functionally linking these two central enzymatic activities required for cell wall peptidoglycan biosynthesis" (PMID 37620344). Thus **glycan polymerization (RodA) and peptide crosslinking (PBP2/MrdA) are physically coupled**.

- **The synthase is organized by the MreB cytoskeleton.** The elongasome/Rod complex "consists of six highly conserved proteins, including the actin-like MreB, the PG synthase complex RodA-PBP2, and three regulatory membrane proteins, MreC, MreD, and RodZ" (Zhan et al. 2026, PMID 42578761). MreB "is localized beneath the cytoplasmic membrane, where it organizes the elongasome complex" (Maharjan et al. 2026, PMID 41802002). PBP2 is coupled directly to this cytoskeleton: "both the cytoplasmic region of PBP2 and the C-terminal tail of RodA interact with MreB … disruption of these interactions results in a loss of rod shape" (Zhan et al. 2026, PMID 42394843).

- **Regulation.** The activity of the RodA–PBP2 synthase is controlled by MreC/MreD and RodZ; "RodZ acts through MreBCD to activate the elongasome" (Zhan et al. 2026, PMID 42578761). In *B. subtilis* the processive circumferential motion of the complex is tuned by RodA levels via a "molecular motor tug-of-war" (Middlemiss et al. 2024, PMID 38926336).

- **Physiological role and redundancy.** New PG is inserted into the **lateral (side) wall** to extend the cylinder of the rod; PBP2 crosslinking is what converts the newly polymerized glycan into load-bearing wall. Inhibition or loss of PBP2 abolishes rod shape (cells round up) and, under growth, leads to lysis. This elongation function is partly buffered by the class A PBP1B: PBP2 inhibition "can be compensated for by the presence of the class A penicillin binding protein, PBP1B" (Grinnell et al. 2022, PMID 35115684), and endopeptidases that cleave existing crosslinks stimulate new synthesis by the Rod system (Lai et al. 2017, PMID 28749938). This division of labour distinguishes MrdA/PBP2 (elongation) from PBP3/FtsI (septation/division), which is the cognate transpeptidase of the FtsW–PBP3 divisome.

- **Organism-specific genomic evidence that mrdA-II is the RodA-coupled elongation PBP2.** In *P. putida* KT2440, the target gene *mrdA-II* (PP_4807) is the second gene of an *mrd* operon whose first gene, **PP_4806 = *mrdB/rodA*** (Q88DL9), encodes the **SEDS peptidoglycan glycosyltransferase RodA** (EC 2.4.99.28) — precisely the obligate synthase partner that, in the cryo-EM structure (PMID 37620344), polymerizes the glycan and delivers it to the PBP2 transpeptidase site. This tight genomic linkage of *mrdA-II* to its cognate *rodA* (mirroring the *E. coli mrdAB* operon) is direct, organism-specific support that PP_4807 is the elongation-specific PBP2 that assembles the **RodA–PBP2 synthase** in this bacterium. The other PBP2 paralog, *mrdA-I* (PP_3741), lacks an adjacent *rodA* and is the divergent/accessory copy.
- ***P. putida* context.** *P. putida* is a rod-shaped organism whose DAP-type peptidoglycan is subject to chemical editing by environmental D-amino acids; work in this species showed that non-canonical D-amino acids (e.g. D-canavanine) can be incorporated and perturb crosslinking and division, with resistance mapping to a division transpeptidase (Aliashkevich et al. 2021, PMID 33830599). This confirms that *P. putida* uses the canonical PBP transpeptidase machinery for wall crosslinking, the elongation arm of which is MrdA/PBP2.

---

## 4. Subcellular localization

MrdA/PBP2 is a **bitopic (single-pass) inner-membrane (cytoplasmic-membrane) protein**:

- **Direct annotation:** UniProt (HAMAP-Rule MF_02081) assigns Q88DL8 to the **"Cell inner membrane; Single-pass membrane protein."** UniProt sequence features locate the single transmembrane helix at **residues 21–41**.
- **Topology (confirmed on Q88DL8 + family-conserved):** a short N-terminal **cytoplasmic tail (res 1–20)**, a single **non-cleaved transmembrane anchor (res 21–41)**, and a large **periplasmic** region (res ~42–629) comprising the pedestal (dimerization) domain (63–236) and the C-terminal transpeptidase domain (268–604).
- **Where catalysis happens:** Lipid II is flipped to the periplasmic (outer) face of the inner membrane, so **the transpeptidase reaction occurs in the periplasm**, on the outer surface of the cytoplasmic membrane, immediately adjacent to the growing sacculus.
- **Where it is positioned:** the enzyme is recruited to discrete, circumferentially moving foci along the lateral cell body by the MreB filament, which lies "beneath the cytoplasmic membrane" (PMID 41802002). The cytoplasmic N-terminus of PBP2 contacts MreB (PMID 42394843), so the single membrane pass allows one molecule to **couple cytoplasmic cytoskeletal positioning to periplasmic wall synthesis**.

Net localization statement: **cytoplasmic (inner) membrane, single-pass, with the catalytic domain projecting into the periplasm; concentrated in mobile lateral-wall elongasome complexes.**

---

## 5. Pathway summary

Peptidoglycan biosynthesis, elongation branch:

UDP-MurNAc-pentapeptide → **Lipid I → Lipid II** (cytoplasmic/inner-leaflet steps, MraY/MurG) → flip to periplasmic face (MurJ) → **RodA glycosyltransfer** (glycan-strand polymerization) → **MrdA/PBP2 D,D-transpeptidation** (4→3 mDAP–D-Ala crosslinking) → mature, load-bearing sacculus.
Spatial control: **MreB–MreC–MreD–RodZ** (Rod complex) direct where and when RodA–PBP2 acts.

MrdA/PBP2 sits at the **crosslinking node** of this pathway, downstream of glycan polymerization and immediately determining the mechanical integrity and rod geometry of the wall.

---

## 6. Evidence quality and hierarchy

- **Direct enzymatic/structural evidence (family, high confidence):** crystal structure and transpeptidase active-site definition of PBP2 (PMID 38581948); cryo-EM mechanism of the RodA–PBP2 synthase (PMID 37620344).
- **Direct genetic/physiological evidence (family, high confidence):** mecillinam/zidebactam target specificity for PBP2 (PMID 25733506, 28749938, 28289035; *Pseudomonas* resistance mutation PMID 42294650); MreB–PBP2 coupling and elongasome organization (PMID 42394843, 42578761, 41802002); redundancy with PBP1B (PMID 35115684).
- **Direct sequence/bioinformatic evidence on Q88DL8 (this study):** the target sequence carries the intact SxxK (Ser327) and K[S/T]G (537–540) catalytic motifs, the single TM anchor (21–41), and the pedestal + transpeptidase domain pair (Pfam PF03717/PF00905; InterPro IPR017790 "PBP2"). Global alignment establishes mrdA-II and mrdA-I (PP_3741) as 70.8%-identical paralogs, both catalytically intact — confirming PP_4807 is a functional, not degenerate, PBP2.
- **Direct genomic-context evidence on PP_4807 (this study):** *mrdA-II* is the second gene of an *mrd* operon with its cognate SEDS partner *mrdB/rodA* (PP_4806) immediately upstream, marking it as the RodA-coupled, elongation-specific PBP2 in *P. putida* (whereas *mrdA-I*/PP_3741 has no adjacent *rodA*).
- ***P. putida*–specific supporting evidence:** DAP-type PG editing and transpeptidase involvement in this organism (PMID 33830599); UniProt "Cell inner membrane; Single-pass membrane protein" annotation for Q88DL8 (HAMAP MF_02081).
- **Inference (annotation-level):** the *physiological* details specific to PP_4807 in cells (essentiality, kinetics, whether it is the principal vs. accessory elongation PBP2, condition-specific deployment) are **not yet measured directly on this locus** and are inferred from family conservation.

## 7. Limitations and future directions

1. **Paralog specificity.** *P. putida* KT2440 encodes two *mrdA*/PBP2 genes — mrdA-I (PP_3741) and mrdA-II (PP_4807, this target) — that are 70.8% identical and both catalytically intact. Genomic context argues that **mrdA-II is the canonical elongation PBP2** (operon-linked to its RodA partner) and mrdA-I the accessory copy, but this has not been tested functionally: the paralogs' relative essentiality, expression conditions, and differential β-lactam/mecillinam sensitivity remain unknown. Targeted single- and double-deletion/complementation of PP_4807 vs PP_3741, Bocillin-FL PBP profiling, and mecillinam-sensitivity assays would resolve this.
2. **Direct biochemistry** (kinetics, Lipid II crosslinking assays, β-lactam acylation rates) on the *P. putida* enzyme itself is lacking.
3. **In-cell localization/dynamics** (fluorescent-fusion tracking of PP_4807 relative to MreB and the second paralog) would confirm elongasome membership for this specific gene product.

---

## 8. Conclusion

*mrdA-II* (PP_4807, Q88DL8) encodes a **Class B penicillin-binding protein 2 (PBP2/MrdA)**, a **single-pass inner-membrane serine D,D-transpeptidase (EC 3.4.16.4; catalytic nucleophile Ser327)** whose primary function is to **crosslink peptidoglycan (4→3 D-Ala–meso-DAP bonds) during cell-wall elongation**. It acts in the **periplasm** as the **cognate transpeptidase of the RodA–PBP2 synthase**, which is polymerized-glycan–fed by the SEDS enzyme RodA and spatially organized by the **MreB/MreC/MreD/RodZ elongasome**, thereby inserting new lateral wall material to maintain the rod shape of *P. putida*. It is the physiological target of the PBP2-specific agents mecillinam and zidebactam. Notably, it is **one of two PBP2 paralogs** in KT2440 (with mrdA-I/PP_3741, 70.8% identical); both are catalytically intact. Genomic context marks **mrdA-II (PP_4807) as the canonical elongation PBP2**, since it is encoded in an *mrd* operon directly downstream of its cognate SEDS glycosyltransferase partner *rodA*/mrdB (PP_4806), whereas mrdA-I lacks an adjacent *rodA*. The precise in-cell division of labour between the two paralogs remains to be tested experimentally.


## Artifacts

- [OpenScientist final report](mrdA-II-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mrdA-II-deep-research-openscientist_artifacts/final_report.pdf)