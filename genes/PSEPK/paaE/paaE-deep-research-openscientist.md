---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T12:43:19.695749'
end_time: '2026-07-23T12:55:29.960044'
duration_seconds: 730.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaE
  gene_symbol: paaE
  uniprot_accession: Q88HS9
  protein_description: 'SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase, reductase
    subunit {ECO:0000313|EMBL:AAN68881.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68881.1};'
  gene_info: Name=paaE {ECO:0000313|EMBL:AAN68881.1}; OrderedLocusNames=PP_3274 {ECO:0000313|EMBL:AAN68881.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 2Fe-2S_ferredoxin-like_sf. (IPR036010); 2Fe-2S_ferredoxin-type.
    (IPR001041); 2Fe2S_fd_BS. (IPR006058); Beta-grasp_dom_sf. (IPR012675); Cbr1-like_FAD-bd_dom.
    (IPR008333)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: paaE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS9
- **Protein Description:** SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase, reductase subunit {ECO:0000313|EMBL:AAN68881.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68881.1};
- **Gene Information:** Name=paaE {ECO:0000313|EMBL:AAN68881.1}; OrderedLocusNames=PP_3274 {ECO:0000313|EMBL:AAN68881.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 2Fe-2S_ferredoxin-like_sf. (IPR036010); 2Fe-2S_ferredoxin-type. (IPR001041); 2Fe2S_fd_BS. (IPR006058); Beta-grasp_dom_sf. (IPR012675); Cbr1-like_FAD-bd_dom. (IPR008333)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaE** (gene ID: paaE, UniProt: Q88HS9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *paaE* (Q88HS9, PP_3274) — Ring 1,2-Phenylacetyl-CoA Epoxidase, Reductase Subunit — in *Pseudomonas putida* KT2440

## 0. Identity verification (target confirmation)

| Field | Value |
|---|---|
| UniProt accession | Q88HS9 |
| Gene symbol | *paaE* |
| Ordered locus | PP_3274 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125), strain PSEPK |
| Annotation | Ring 1,2-phenylacetyl-CoA epoxidase, reductase subunit; EC 1.14.13.149 |
| Key domains | Plant-type **[2Fe-2S] ferredoxin** (IPR001041/IPR006058/IPR036010); **β-grasp/NAD-binding** scaffold (IPR012675); **Cbr1-like FAD-binding** oxidoreductase domain (IPR008333) |

**The identification is unambiguous and internally consistent.** The gene symbol *paaE* is the standard name for the reductase subunit of the phenylacetyl-CoA (PA-CoA) oxygenase across bacteria (E. coli, *Pseudomonas*, *Azoarcus*), and the *paa* gene cluster is conserved. The three cofactor-binding modules encoded by Q88HS9 — an FAD-binding domain, an NAD(P)H/β-grasp module, and a plant-type [2Fe-2S] ferredoxin domain — are the textbook architecture of a **flavo-ferredoxin NAD(P)H:acceptor oxidoreductase (reductase)**, the same fold family used by the reductase components of bacterial multicomponent oxygenases. This matches the UniProt description (reductase subunit; EC 1.14.13.149) exactly. No conflicting gene named *paaE* with a different function was found. The report below therefore proceeds with high confidence.

---

## 1. Summary (answer to the research question)

*paaE* encodes the **reductase (electron-transfer) subunit of the multicomponent ring-1,2-phenylacetyl-CoA epoxidase (oxygenase)** that carries out the single committed oxygen-dependent step of the aerobic "hybrid" phenylacetate/phenylalanine catabolic pathway in *P. putida* KT2440. PaaE is a soluble, **cytoplasmic** NAD(P)H-dependent oxidoreductase that uses its FAD and [2Fe-2S] cofactors to shuttle reducing equivalents from **NAD(P)H → FAD → [2Fe-2S] cluster → the diiron active site of the PaaA/PaaC oxygenase core**. This electron supply enables the oxygenase to activate molecular O₂ and **epoxidize the aromatic ring of phenylacetyl-CoA to a non-aromatic ring-1,2-epoxide** (EC 1.14.13.149), which subsequently isomerizes to oxepin-CoA and is degraded to acetyl-CoA and succinyl-CoA. Its substrate specificity is defined by the complex: the oxygenized substrate is the **CoA thioester of phenylacetate (phenylacetyl-CoA)**, while PaaE's own redox substrate is **NAD(P)H**.

---

## 2. Biochemical function — what reaction is catalyzed, and substrate specificity

### 2.1 The enzyme complex and PaaE's specific role
The oxygenation of the aromatic ring in this pathway is performed not by a single protein but by a **multicomponent oxygenase encoded by *paaABCDE***. Biochemical dissection of the homologous *E. coli* system established the roles of the subunits:

- **PaaA** — catalytic α-subunit bearing the **carboxylate-bridged diiron center** where O₂ is activated and the substrate is oxidized.
- **PaaC** — structural β-subunit; PaaA and PaaC together form the catalytic heterotetrameric core (PaaAC).
- **PaaB** — small accessory subunit required for activity.
- **PaaE** — the **reductase**: an NAD(P)H:oxidoreductase carrying FAD and a [2Fe-2S] cluster that feeds electrons into the diiron oxygenase.
- **PaaD** — a putative [Fe-S] chaperone/assembly factor; **not essential** for in vitro catalysis.

In vitro reconstitution showed that "**each of the PaaA, B, C, and E subunits are necessary for catalysis, whereas PaaD is not essential**" (Grishin et al. 2011). Thus PaaE is an obligatory component: without the reductase, the diiron center cannot be re-reduced between turnovers and no oxygenation occurs.

### 2.2 Overall reaction (EC 1.14.13.149)
The complex catalyzes:

> **phenylacetyl-CoA + NADPH + H⁺ + O₂ → 1,2-epoxyphenylacetyl-CoA (ring-1,2-epoxide) + NADP⁺ + H₂O**

PaaE's partial reaction is the **oxidation of NAD(P)H and delivery of two electrons** (one at a time, via FAD semiquinone chemistry and the one-electron [2Fe-2S] carrier) to the oxygenase. This is the classic division of labour in bacterial multicomponent monooxygenase/dioxygenase systems: a flavo-ferredoxin **reductase** (PaaE) + a **diiron oxygenase** (PaaA/PaaC) + accessory subunit(s).

### 2.3 Substrate specificity
- **Oxidized substrate of the complex:** the **coenzyme A thioester of phenylacetate** (phenylacetyl-CoA), not free phenylacetate. Intermediates in this entire pathway are handled as CoA thioesters, a defining feature that distinguishes it from classical aerobic aromatic catabolism (Ismail et al. 2003; Teufel et al. 2010). This CoA-activation is imposed upstream by the phenylacetate-CoA ligase (PaaK/PaaF-type ligase).
- **Redox cosubstrate of PaaE:** **NAD(P)H** (the annotated EC uses NADPH); electron acceptor is molecular O₂ at the oxygenase diiron site.
- **Product:** a **ring-1,2-epoxide of phenylacetyl-CoA** — a reactive, *non-aromatic* epoxide. This is mechanistically distinct from ring-hydroxylating dioxygenases, which make cis-dihydrodiols/catechols. As Ismail et al. put it, the pathway generates "a hydroxylated and reduced derivative of phenylacetyl-CoA, which is **not re-oxidized to a dihydroxylated aromatic intermediate**, as in other known aromatic pathways."

### 2.4 Structural/mechanistic evidence for the electron-transfer role
The crystal structure of the PaaAC catalytic core (E. coli) revealed a monooxygenase fold organized "**very differently from other known multisubunit monooxygenases**" and, importantly, that it "**lacks their conservative network of hydrogen bonds between the di-iron center and protein surface, suggesting different association with the reductase and different mechanisms of electron transport**" (Grishin et al. 2011). This directly implicates a dedicated reductase (PaaE) whose docking and electron-relay to the diiron center is a distinguishing property of the Paa oxygenase subfamily. The reductase's own cofactor set — **FAD (2-electron/NAD(P)H interface) + [2Fe-2S] (1-electron output)** — is exactly what is required to interconvert the two-electron chemistry of NAD(P)H and the one-electron chemistry of the diiron/O₂ system.

---

## 3. Pathway context — where PaaE functions biochemically

PaaE performs the **committed, rate-defining oxygenation step** of the widespread aerobic "hybrid" phenylacetate pathway (the *phenylacetyl-CoA catabolon*). The full route (Teufel et al. 2010; Ismail et al. 2003; Ferrández et al. 1998; Teufel et al. 2011):

1. **Activation:** phenylacetate + CoA + ATP → **phenylacetyl-CoA** (phenylacetate-CoA ligase; PaaK/PaaF).
2. **Ring epoxidation (PaaE step):** phenylacetyl-CoA → **ring-1,2-epoxyphenylacetyl-CoA** by the *paaABCDE* oxygenase, with PaaE supplying electrons from NAD(P)H. *(EC 1.14.13.149)*
3. **Isomerization:** the non-aromatic epoxide → **oxepin-CoA** (a seven-membered O-heterocyclic enol ether) by the isomerase (PaaG-type).
4. **Ring hydrolysis:** oxepin-CoA → 3-oxo-5,6-dehydrosuberyl-CoA by the bifunctional **PaaZ** (enoyl-CoA hydratase + aldehyde dehydrogenase) (Teufel et al. 2011).
5. **β-oxidation-like steps** (PaaF/G/H/J) → **acetyl-CoA + succinyl-CoA**, feeding the TCA cycle.

This pathway is a **"hybrid" aerobic route**: it requires O₂ (via PaaABCDE) yet, unusually, does *not* use an oxygenase for ring *cleavage* — the ring is opened hydrolytically (Fuchs 2008). PaaE is the electron-delivery engine that makes the one oxygen-dependent step possible. Because phenylalanine and styrene are funneled to phenylacetate, PaaE also lies on the terminal common route of **phenylalanine and styrene catabolism**. This pathway operates in "**16% of all bacteria whose genome has been sequenced, including Escherichia coli and Pseudomonas putida**" (Teufel et al. 2010), placing PaaE firmly in *P. putida* KT2440 physiology.

**Regulation/genomic context:** the *paaABCDE* genes are part of a large *paa* operon/cluster; in *E. coli* the operon is induced by phenylacetyl-CoA (the true inducer) via the PaaX repressor (Ferrández et al. 1998). The same catabolon logic — CoA-thioester induction and a conserved gene cluster — applies in *Pseudomonas*.

---

## 4. Subcellular localization

PaaE is a **soluble cytoplasmic protein**. Multiple lines of evidence support this:
- The entire phenylacetate/phenylalanine hybrid pathway processes **intracellular CoA thioesters** (Teufel et al. 2010; Ismail et al. 2003); CoA-thioester metabolism is inherently cytoplasmic because CoA does not cross the membrane, and its substrate is generated by a cytoplasmic CoA ligase.
- PaaE was expressed and reconstituted as a soluble subunit in vitro together with the other Paa subunits (Grishin et al. 2011), consistent with a cytosolic, non-membrane enzyme.
- The domain architecture (FAD/NAD(P)H/[2Fe-2S] reductase) carries **no signal peptide or transmembrane segment**, matching a cytoplasmic redox protein.

Functionally, PaaE acts at the **cytoplasmic face**, transiently docking onto the PaaA/PaaC oxygenase to transfer electrons.

---

## 5. Evolutionary / bioinformatic inference

- **Domain-based inference:** the FAD-binding (Cbr1/ferredoxin-NADP⁺-reductase–like), NAD-binding β-grasp, and plant-type [2Fe-2S] ferredoxin domains define a **reductase of the class-I(A)/glutathione-reductase-like flavo-ferredoxin family** that partners diiron/Rieske oxygenases. This places PaaE alongside well-characterized reductase components of bacterial multicomponent oxygenases and is fully consistent with the assigned reductase role.
- **Orthology/conservation:** *paaE* orthologs co-occur with *paaABCD* in a conserved cluster across diverse phyla (E. coli *paaABCDEFGHIJK*; *Azoarcus evansii paaYZGHIKABCDE*; *P. putida paa*), and their gene products are mutually "similar to the characterized putative gene products involved in PA catabolism in *E. coli* and *Pseudomonas putida*" (Mohamed et al. 2002). Conserved synteny with the oxygenase genes is strong evidence that PaaE is the dedicated reductase of this specific oxygenase.

---

## 6. Supported vs. refuted hypotheses

**Supported**
- H1 (supported): PaaE is the **reductase subunit** of the PA-CoA epoxidase and is **essential** for oxygenase activity (Grishin et al. 2011; Ismail et al. 2003; Ferrández et al. 1998).
- H2 (supported): The complex epoxidizes the **aromatic ring of phenylacetyl-CoA** to a non-aromatic ring-1,2-epoxide using O₂ and NAD(P)H (Teufel et al. 2010; EC 1.14.13.149).
- H3 (supported): PaaE functions **in the cytoplasm** as part of a CoA-thioester–based pathway (Teufel et al. 2010; Ismail et al. 2003).
- H4 (supported): The pathway is a **hybrid aerobic route** (O₂ used for ring activation, not ring cleavage) that yields acetyl-CoA + succinyl-CoA (Fuchs 2008; Teufel et al. 2011).

**Refuted / excluded**
- Not a ring-hydroxylating dioxygenase producing catechols/dihydrodiols — the product is an epoxide that isomerizes to oxepin-CoA, and no dihydroxy-aromatic is formed (Ismail et al. 2003; Teufel et al. 2010).
- PaaE is **not** the non-essential accessory factor — that role belongs to **PaaD** (Grishin et al. 2011).

---

## 7. Limitations and future directions

- Most direct biochemical/structural data (subunit reconstitution, PaaAC crystal structure) come from the **E. coli** ortholog; while the *P. putida* KT2440 *paa* cluster is orthologous and the pathway is confirmed present in *P. putida* (Teufel et al. 2010), a dedicated crystal structure or steady-state kinetic characterization of the specific *P. putida* KT2440 PaaE (Q88HS9) protein was not identified.
- The precise cofactor stoichiometry (FAD vs. FMN; measured [2Fe-2S] EPR signature) and NADH-vs-NADPH preference of the *P. putida* enzyme have not, to my knowledge, been individually reported and would be worth measuring.
- A high-resolution PaaE–oxygenase docking model / electron-transfer pathway remains an open structural question flagged by Grishin et al. (2011).

---

## References (PMIDs)
- Teufel R, Mascaraque V, Ismail W, et al. **Bacterial phenylalanine and phenylacetate catabolic pathway revealed.** *PNAS* 2010. **PMID 20660314.**
- Grishin AM, Ajamian E, Tao L, et al. **Structural and functional studies of the *E. coli* phenylacetyl-CoA monooxygenase complex.** *J Biol Chem* 2011. **PMID 21247899.**
- Ismail W, El-Said Mohamed M, Wanner BL, et al. **Functional genomics by NMR spectroscopy. Phenylacetate catabolism in *E. coli*.** *Eur J Biochem* 2003. **PMID 12846838.**
- Ferrández A, Miñambres B, García B, et al. **Catabolism of phenylacetic acid in *E. coli*. Characterization of a new aerobic hybrid pathway.** *J Biol Chem* 1998. **PMID 9748275.**
- Teufel R, Gantert C, Voss M, et al. **Studies on the mechanism of ring hydrolysis in phenylacetate degradation (PaaZ).** *J Biol Chem* 2011. **PMID 21296885.**
- Fuchs G. **Anaerobic metabolism of aromatic compounds.** *Ann N Y Acad Sci* 2008. **PMID 18378589.**
- Mohamed ME, Ismail W, Heider J, Fuchs G. **Aerobic metabolism of phenylacetic acids in *Azoarcus evansii*.** *Arch Microbiol* 2002. **PMID 12189419.**


## Artifacts

- [OpenScientist final report](paaE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaE-deep-research-openscientist_artifacts/final_report.pdf)