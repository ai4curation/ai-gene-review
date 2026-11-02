# MFGE8 (lactadherin) – curation notes

**Provenance note:** Provider deep research failed (Falcon returned HTTP 402 Payment
Required; Perplexity not configured). No `-deep-research-<provider>.md` file exists. The
synthesis below replaces it and was assembled manually from the UniProt record (Q08431),
cached publications in `publications/`, and PubMed searches (E-utilities) used only to locate
PMIDs, which were then cached with `just fetch-gene-pmids human MFGE8`.

## Identity and architecture

- UniProt Q08431, lactadherin / MFG-E8 / BA46 / SED1; secreted glycoprotein, 387 aa precursor
  (signal peptide 1-23). Human protein has one N-terminal EGF-like domain (24-67) carrying the
  RGD integrin-binding motif (46-48), followed by two discoidin (F5/8 type C) domains, C1
  (70-225) and C2 (230-387). (UniProt FT lines.)
- UniProt: "The F5/8 type C 2 domain mediates high-affinity binding to phosphatidylserine-containing
  membranes" (ECO:0000250).
- Chains: lactadherin (24-387), lactadherin short form (202-387), and **medin** (268-317).
- Mouse Mfge8 has two EGF domains; the RGD sits in EGF2 [PMID:19204935 "The second EGF domain
  also contains an arginine-glycine-aspartic acid (RGD) integrin-binding motif that engages αvβ3/5
  integrin heterodimers"]. Human has a single EGF domain with the RGD.

## Core activity: phosphatidylserine-bridging opsonin

- Discovery (mouse): [PMID:12000961 "MFG-E8 specifically bound to apoptotic cells by recognizing
  aminophospholipids such as phosphatidylserine. MFG-E8, when engaged by phospholipids, bound to
  cells via its RGD (arginine-glycine-aspartate) motif--it bound particularly strongly to cells
  expressing alpha(v)beta(3) integrin."] An RGE mutant acts as dominant negative and blocks
  macrophage engulfment in vitro and in vivo.
- In vivo requirement (mouse): [PMID:15155946 "These data demonstrate that MFG-E8 has a critical
  role in removing apoptotic B cells in the germinal centers and that its failure can lead to
  autoimmune diseases."]
- Domain logic: C-terminal discoidin domains bind PS; RGD binds αv integrins on the phagocyte
  [PMID:19204935 "The C-terminal domains mediate attachment to phosphatidylserine and
  phosphatidylethanolamine residues exposed on the surface of the apoptotic lymphocyte, whereas
  the RGD motif binds to αv integrins expressed on the advancing phagocyte"].
- Human protein: [PMID:19204935 "the human homolog of SED1/MFG-E8 (hMFG-E8) also binds
  phosphatidylserine and engages αvβ3 integrins"]; human SLE-associated truncation mutant still
  [PMID:20213738 "bound to phosphatidylserine and enhanced the phagocytosis of apoptotic cells"].
- Structural basis (bovine C2 domain, 1.7 Å) [PMID:18160406 "Lactadherin is a
  phosphatidyl-L-serine (Ptd-L-Ser)-binding protein that decorates membranes of milk fat
  globules. The major Ptd-l-Ser binding function of lactadherin has been localized to its C2
  domain"]. Lactadherin also competes with factors V/VIII for PS sites and is anticoagulant in
  vitro (same abstract).
- Lactadherin is used as a PS probe, detecting low-density PS exposure earlier than annexin V
  [PMID:17123296 "Macrophages secrete lactadherin, a PS-binding protein, which tethers apoptotic
  cells to macrophage integrins."].
- Human genetics: rare intronic MFGE8 variant creating a cryptic exon in 2/322 female SLE patients
  [PMID:20213738].

## Neuronal / synaptic opsonization (phagoptosis)

- [PMID:22357850 "MFG-E8 ... is known to mediate the phagocytic removal of apoptotic cells by
  bridging phosphatidylserine (PS)-exposing cells and the vitronectin receptor (VR) on
  phagocytes"]; in LPS neuroinflammation, MFG-E8 drives microglial phagocytosis of *viable*
  neurons; neuronal loss absent in Mfge8 KO cultures and restored by recombinant MFG-E8 (mouse/rat).
- Aβ-induced neuronal loss in mixed cultures is MFG-E8 dependent [PMID:23647050 "this neuronal
  loss is mediated by the bridging protein lactadherin/milk-fat globule epidermal growth
  factor-like factor 8 (MFG-E8), which is released by Aβ-activated microglia, binds to co-cultured
  neurons and opsonizes neurons for phagocytosis by microglia"].
- Human AD (ex vivo / cultured human glia): synaptoneurosomes from AD brain carry more MFG-E8;
  blocking the integrin-binding site of MFG-E8 reduces astrocytic and microglial ingestion of AD
  (but not control) synapses; blocking astrocytic integrin αvβ5 has a similar effect
  [PMID:37652017 "AD promotes increased synapse ingestion by human glial cells at least in part via
  an MFG-E8 opsonophagocytic mechanism"; "One possible mechanism for tagging synapses for ingestion
  is via MFG-E8, a phosphatidylserine-recognizing opsonin."]. Note: PS on the synapses was not
  directly measured in this paper; the PS link is inferred ("MFG-E8 protein is likely increased on
  AD synapses due to binding phosphatidylserine").
- **Curation caveat (for cross-checking downstream disease models):** MFG-E8 is not a complement
  component; its synapse-tagging mechanism is PS-bridging to integrins (αvβ3/αvβ5), parallel to
  but distinct from C1q/C3-mediated pruning. Grouping it under a "complement-mediated" node is a
  mechanistic simplification.

## Other roles (mostly mouse, non-core for GO MF)

- Intestinal epithelial repair: [PMID:18008006 "MFG-E8 bound to phosphatidylserine and triggered
  reorientation of the actin cytoskeleton in intestinal epithelial cells at the wound edge."]
- VEGF-dependent neovascularization via αvβ3/αvβ5 [PMID:15834428 "lactadherin interacts with
  alphavbeta3 and alphavbeta5 integrins and alters both VEGF-dependent Akt phosphorylation and
  neovascularization"].
- Collagen uptake / anti-fibrotic (mouse) [PMID:19884654 "Mfge8 directly bound collagen and that
  Mfge8-/- macrophages exhibited defective collagen uptake that could be rescued by recombinant
  Mfge8 containing at least one discoidin domain"].
- Sperm–zona pellucida adhesion (pig/mouse SED1) [PMID:19204935 "SED1/MFG-E8-null male mice, which
  are sub-fertile in vivo and whose sperm are unable to bind eggs in vitro"]; sperm-associated
  protein is largely epididymal and sits on the anterior dorsal plasma membrane over the acrosome.

## Medin (vascular amyloid)

- [PMID:10411933 "We found that the main constituent of aortic medial amyloid is a 50-aa-long
  peptide, here called medin, that is positioned within the coagulation factor-like domain of
  lactadherin."] Aortic medial amyloid occurs in virtually all individuals over 60; lactadherin
  is made by aortic medial smooth muscle cells.
- Medin aggregation causes cerebrovascular dysfunction in aged wild-type mice [PMID:32900929].
- [PMID:36385530 "Mechanistically, we demonstrate that medin interacts directly with amyloid-β to
  promote its aggregation, as medin forms heterologous fibrils with amyloid-β, affects amyloid-β
  fibril structure, and cross-seeds amyloid-β aggregation both in vitro and in vivo."] Medin
  co-localizes with vascular Aβ (CAA); medin deficiency halves vascular Aβ in mice; MFGE8
  expression rises in AD (ROSMAP).
- Medin formation is pathological/age-related, not a physiological GO function of the gene
  product; captured in description only.

## Annotation review summary decisions

- PS binding (IBA, IPI) and integrin binding (IEA) – ACCEPT; core bridging activities.
- Apoptotic cell clearance (IEA from mouse) – ACCEPT; core BP.
- ECM structural constituent (RCA, matrisome-based ×4) – MARK_AS_OVER_ANNOTATED: MFG-E8 is a
  soluble bridging opsonin; no structural role.
- Extracellular region / external side of PM / membrane – ACCEPT or non-core.
- Exosome / EV / ECM HDA, interstitial matrix TAS, acrosomal membrane IEA, ER lumen TAS
  (FAM20C reaction, transit) – KEEP_AS_NON_CORE.
- No NEW annotations proposed. "Synapse pruning" was considered but evidence is limited to an
  antibody-blocking assay in a disease context; raised as a question instead.
