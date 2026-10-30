# FANCI (Q9NVI1) review notes

Human Fanconi anemia group I protein. HGNC:25568. 1328 aa. Chromosome 15.

## Core biology (synthesized)

FANCI is the obligate heterodimeric partner of FANCD2, forming the FANCI-FANCD2
(ID2) complex, the central effector of the Fanconi anemia (FA) DNA-repair pathway.
Both proteins are monoubiquitinated (FANCI on Lys523) by the FANCL/UBE2T ligase
acting downstream of the multi-subunit FA core complex. Monoubiquitination is
mutually interdependent, and FANCI is required to promote FANCD2 monoubiquitination.
The ID2 complex binds and scans dsDNA with preference for branched structures
(Holliday junctions, overhangs, replication forks); upon monoubiquitination it
rearranges into a closed sliding clamp that encircles duplex DNA to coordinate ICL
repair (nucleolytic incision/unhooking, translesion synthesis, homologous
recombination). FANCI phosphorylation by ATR (S/TQ cluster) acts as a molecular
switch turning the pathway on. Disease: Fanconi anemia complementation group I
(biallelic FANCI mutations).

## Provenance

- Identity / paralog / monoubiquitination at K523 / FANCD2 interaction:
  [PMID:17460694 "A FANCD2 protein sequence-based homology search facilitated the discovery of FANCI, a second monoubiquitinated component of the FA pathway. Biallelic mutations in the gene coding for this protein were found in cells from four FA patients, including an FA-I reference cell line."]

- ID2 complex required for ICL repair; monoubiquitination essential:
  [PMID:32269332 "The ID complex, involving the proteins FANCI and FANCD2, is required for the repair of DNA interstrand crosslinks (ICL) and related lesions"]
  [PMID:32269332 "Monoubiquitination of ID is essential for ICL repair by excision, translesion synthesis and homologous recombination"]

- DNA clamp / encircles DNA:
  [PMID:32269332 "we report a cryo-electron microscopy structure of the monoubiquitinated human ID complex bound to DNA, and reveal that it forms a closed ring that encircles the DNA"]
  [PMID:32269332 "the monoubiquitinated ID complex loses its preference for ICL and related branched DNA structures, and becomes a sliding DNA clamp that can coordinate the subsequent repair reactions"]

- DNA binding, preference for branched DNA:
  [PMID:32269332 "FANCI and FANCD2 are paralogs that bind to DNA with preference for branched structures including Holliday junction, overhang and replication fork DNA"]

- FANCI required for replication-coupled ICL repair in S phase:
  [PMID:19965384 "Using a cell-free system, we showed that FANCI-FANCD2 is required for replication-coupled ICL repair in S phase."]
  [PMID:19965384 "A central event in the activation of the Fanconi anemia pathway is the mono-ubiquitylation of the FANCI-FANCD2 complex"]

- FANCI phosphorylation = molecular switch that promotes FANCD2 monoubiquitination:
  [PMID:18931676 "FANCI carrying phosphomimic mutations on the same six residues induces constitutive monoubiquitination and focus formation of FANCI and FANCD2, and protects against cell killing and chromosome breakage by DNA interstrand cross-linking agents. We propose that the multiple phosphorylation of FANCI serves as a molecular switch in activation of the Fanconi anemia pathway."]
  [PMID:18931676 "FANCI phosphorylation exerts an evolutionarily conserved function in inducing FANCD2 monoubiqutination in human cells as well."]

- FANCD2 monoubiquitination targets ID to chromatin:
  [PMID:18931676 "In turn, FancD2 and FancI are both targeted to chromatin and form colocalizing foci together with the HR proteins BRCA1 and Rad51"]

- FAN1 interaction (FAN1 recruited by monoubiquitinated FANCD2; FANCI co-purifies):
  [PMID:20603015 "a highly conserved protein, KIAA1018/MTMR15/FAN1, that interacts with, and is recruited to sites of DNA damage by, the monoubiquitinated form of FANCD2"]

- POLN interaction / role in crosslink repair and HR:
  [PMID:19995904 "we obtained evidence for physical and functional interaction of POLN with factors belonging to the Fanconi anemia pathway, a master regulator of cross-link repair"]

- CTDP1 interaction / regulation of FANCI:
  [PMID:31240132 "CTDP1 was found to regulate multiple aspects of FANCI activity, including chromatin localization, interaction with γ-H2AX, and SQ motif phosphorylations."]

## Localization caveats

- Cytoplasm (UniProt SL / IDA PMID:18445686): PMID:18445686 is an EML3-focused
  mitotic-spindle proteomics paper; FANCI is overwhelmingly a nuclear DNA-repair
  protein. Cytoplasmic annotation is at best a minor/incidental pool -> over-annotated.
- Membrane GO:0016020 (HDA PMID:19946888): from a bulk NK-cell membrane-fraction
  mass-spec survey. FANCI has NO transmembrane region (UniProt) and is a soluble
  nuclear protein. The paper itself notes ~60% of identified proteins are NOT
  plausible membrane proteins and are "transiently associated with membranes"
  [PMID:19946888 "approximately 40% of the identified proteins were predicted as plausible membrane proteins. The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes."]
  -> co-purification artifact; REMOVE.

## MF gap

GOA export lacks a DNA-binding MF term for FANCI even though UniProt carries the
DNA-binding keyword and DNA binding is FANCI's defining biochemical activity
(branched/duplex DNA binding; clamp). Added GO:0003677 as NEW.
</content>


## 2026-10-25 — Integrated evidence, core and current source contexts

The current biological assessment distinguishes FANCI's DNA-binding and ID2 structural/regulatory contribution from FANCL/UBE2T ubiquitin-transfer chemistry. Human ID2 can close with ubiquitin on FANCD2 alone; the old shorthand that FANCI Lys523 ubiquitination always drives closure is not a universal prerequisite. The core retains DNA secondary-structure binding, with broader DNA repair supported independently by the human I-SceI HR-reporter experiments in PMID:17412408. The ICL descendant is not redundantly listed beside that broader process. Human phosphosite and purified chicken K525R/Ex6 experiments support performed promotion of FANCD2 monoubiquitination rather than merely substrate necessity. Chicken Ex6 is the DNA-binding-defective charge-reversal mutant; R1288Q alone retains DNA binding and is not equated to the reported human R1285Q behavior.

Four natural products remain distinct from historical 1328-residue “isoform 1,” fragments and engineered mutants. HPA supports a cytosolic pool without resolving every product or its function. The NK-cell membrane-fraction annotation remains UNDECIDED because its original target table and fraction controls were not recovered; possible carryover is not proven contamination.

The genuine current GOA now has 30 imported contexts, plus retained authored proposal 29: 31 stored objects. Eleven genuine supporting-entity backfills preserve the original source identities. Position 8 takes the seeder's FANCD2 representative, and the separate FAN1 context is appended at 30, leaving every inherited position and all 23 quotation associations intact. No new quotation fields or authored annotations were added. Current actions are 20 ACCEPT / 5 MODIFY / 4 KEEP_AS_NON_CORE / 1 UNDECIDED / 1 retained NEW. The old UniProt machine record remains exact; GOA adoption is explicit. Historical description/status and earlier journal assertions above remain historical, not simultaneous current conclusions.

Five whole reference unions retain the historical note once and both complete labeled current source-reading scopes. All selected publication availability flags were reconciled against immutable cache headers, separately from external availability and actual reading. See the consolidated [FANCI evidence and source guide](FANCI-source-guide.md) for primary Methods/Results/figure locators, the 25 Reactome target paths and three modification states, PAINT ancestry, and access limits. This entry is agent-authored; no provider output is synthesized.

## 2026-10-25 — Canonical validation

All six canonical checks pass, including current GOA matching, term/component validation and rendering of 68 narratives. Computed status is DRAFT with 4 advisories: 3 supported generic-binding advisories retained under the standing campaign instruction and one advisory for the unused inherited research file. Review all 30 current imported contexts and the retained inherited DNA-secondary-structure-binding proposal: 20 ACCEPT, five MODIFY, four KEEP_AS_NON_CORE, one UNDECIDED and one NEW. Retain four natural products without assuming functional equivalence. Keep the membrane-fraction claim UNDECIDED because target-level original evidence remains unavailable. Adopt genuine current GOA with eleven supporting-entity backfills and one appended FAN1 context; retain FANCD2 at old position 8. Preserve all 30 inherited positions, 23 quotation associations, 27 original reference identities and three original core quotation objects; add three supporting references. Existing UniProt, publication/Reactome/family caches, provider outputs, prior history, generated HTML and unrelated work remain exact. New publication files are genuine additive fetches; no new quotation field is authored.


## 2026-10-26 — PR 5548 feedback follow-up

Replace the core DNA-repair parent with the specific ICL-repair term; retain the accepted broad imported annotation and human HR-reporter evidence. The current biological description now includes nucleolar, RNA and FANCD2-independent functions with primary-source scope documented in the source guide. Product/reagent equivalence limits belong in these notes and that guide rather than in the standalone description. The four natural products remain unchanged and are not assumed functionally equivalent.

The earlier integration choice of the broad core process is superseded by this specific-core decision. Seven genuine additional primary caches support the bounded literature audit; the immutable Affinage file was used for discovery and is now explicitly referenced. No new process annotation is added. The separately reviewed human nucleolus IDA assertion is appended at position 31, leaving all earlier positions intact. The three supported generic-binding decisions and membrane UNDECIDED are retained. Shared Reactome provenance is consolidated in the source guide, and spacing artifacts in reviewer-authored reference notes are corrected. All 31 annotation positions, machine source fields and 23 inherited quotation paths/text/reference associations are preserved. No publication quotations were added.

Canonical validation of the accepted successor: All six canonical checks pass and all 70 narratives render. Computed status remains DRAFT with four advisories: three supported generic-binding records under the explicit project instruction and one annotation-level unused-research-file advisory. There are now 32 active objects: 30 imported contexts, the inherited DNA-binding proposal and the appended human nucleolus IDA proposal. All 23 inherited quotation/path/reference associations and four natural products remain unchanged. Nine reference entries are added, yielding 39; seven missing primary publications are genuine additive fetches. The Affinage file is used for discovery and cited at reference level, which does not suppress the annotation-level advisory. No new process annotation or publication quotation is authored.
