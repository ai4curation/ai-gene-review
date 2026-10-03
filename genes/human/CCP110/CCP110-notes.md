# CCP110 (CP110) curation notes

## Deep research status
- `just deep-research-falcon human CCP110` was run (first with `--fallback perplexity-lite`, which is not available in this environment, then with `--timeout 2400`). See the end of this file for the outcome. The review was written from the cached primary literature in `publications/`.

## Key findings (with provenance)
- Centrosomal CDK substrate required for centrosome duplication [PMID:12361598 "RNAi-mediated depletion of CP110 indicates that this protein plays an essential role in centrosome duplication."]
- Required for PLK4-driven procentriole formation; caps growing distal tips [PMID:17681131 "CP110 was recruited early and then associated with the growing distal tips, indicating that centrioles elongate through insertion of alpha-/beta-tubulin underneath a CP110 cap."]; [PMID:16244668 "Plk4 is required--in cooperation with Cdk2, CP110 and Hs-SAS6--for the precise reproduction of centrosomes during the cell cycle"]
- Direct microtubule plus-end capping activity, counteracted by CPAP [PMID:39847124 "We found that whereas CEP97 does not bind to microtubules directly, CP110 autonomously binds microtubule plus ends, blocks their growth, and inhibits depolymerization."]
- Suppresses ciliogenesis with CEP97 [PMID:17719545 "loss of Cep97 or CP110 promotes primary cilia formation in growing cells, and enforced expression of CP110 in quiescent cells suppresses their ability to assemble cilia"], partly through CEP290 [PMID:18694559 "Interaction with CEP290 is absolutely required for the ability of CP110 to suppress primary cilia formation."]
- Cap anchoring: KIF24 -> MPHOSPH9 -> CEP97 -> CP110; TTBK2 phosphorylation of MPP9 triggers its degradation and cap removal [PMID:30375385 "After phosphorylation by Tau Tubulin Kinase 2 (TTBK2) at the beginning of ciliogenesis, MPP9 is targeted for degradation via the ubiquitin-proteasome system, which facilitates the removal of CP110 and CEP97 from the distal end of the mother centriole."]; [PMID:23141541 "TTBK2 acts at the distal end of the basal body, where it promotes the removal of CP110, which caps the mother centriole"]
- Levels controlled by SCF(cyclin F) and USP33 [PMID:20596027 "CP110 is ubiquitylated by the SCF(Cyclin F) ubiquitin ligase complex, leading to its degradation"]; [PMID:23486064 "excessive CP110 drives centrosome over-duplication and suppresses ciliogenesis, whereas its depletion inhibits centriole amplification"]
- Cytokinesis role via calmodulin/centrin [PMID:16760425 "Importantly, expression of a CP110 mutant unable to bind CaM also promotes cytokinesis failure and binucleate cell formation."]
- In vivo pro-ciliogenic role in mouse (source of the ISS rows) [PMID:26965371 "Here, we demonstrate that CP110 promotes cilia formation in vivo, in contrast to findings in cultured cells."]; [PMID:26965371 "Our data implicate CP110 in SDA assembly and ciliary vesicle docking, two requisite early steps in cilia formation."]

## Curation decisions (summary)
- 34 protein binding IPIs: REMOVE (uninformative), except 3 calmodulin rows -> MODIFY to calmodulin binding (GO:0005516).
- Centrosome/centriole, centriole replication, centrosome duplication, negative regulation of cilium assembly, microtubule binding: ACCEPT.
- Positive regulation of cilium assembly (ISS from mouse) and regulation of cytokinesis: KEEP_AS_NON_CORE (context-dependent/secondary).
- Reactome cytosol rows: KEEP_AS_NON_CORE.
- NEW: microtubule plus-end binding (GO:0051010) and regulation of centriole elongation (GO:1903722), both from PMID:39847124. Participation test: CP110 itself caps the plus end (does the work). Comparator: CCP110 orthologs in other species already carry the child term negative regulation of centriole elongation (QuickGO).

## HPA cilium atlas vs module role
- Module (modules/primary_cilium_life_cycle.yaml, stage 1_basal_body_licensing): CCP110 is a "distal centriole cap (ciliogenesis suppressor)" component of the CP110-CEP97 cap, with process negative regulation of cilium assembly and location ciliary basal body.
- HPA v25 (projects/HUMAN_PROTEIN_ATLAS/cilium_life_cycle/member_evidence.md): only "Centriolar satellite (A)"; main location centriolar satellite. No basal body, centrosome or cilium call. The HPA cilium atlas (Hansen et al. 2025, PMID:41005307) is cached abstract-only, so gene-level details cannot be checked there.
- Assessment: the HPA call disagrees with the extensive literature placing CP110 at distal centriole ends (both centrioles in cycling cells, lost from the mother centriole at ciliogenesis). Because the cap is removed from the mother centriole before/at cilium formation, a basal body signal would not be expected in ciliated HPA cells, which may partly explain the absence of a basal-body call; the satellite signal may be a genuine pool or an antibody issue. I keep the module role (negative regulation of cilium assembly at the mother centriole distal end) as a core function; I would quibble with "ciliary basal body" as the module location, since the cap acts on the mother centriole before it becomes a basal body ("centriole" is used in core_functions).
