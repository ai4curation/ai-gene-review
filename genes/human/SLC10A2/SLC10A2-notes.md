# SLC10A2 (ASBT / IBAT / ISBT) curation notes

## Provenance of this review

Automated deep research is **not available in this container**, so the literature
synthesis below was assembled by hand from the cached publications in `publications/`,
the cached Reactome entries, the UniProt record, PANTHER/PAINT donor tracing and
QuickGO comparator queries:

- Falcon/Edison deep-research API returns `402 Payment Required`.
- OpenAI deep-research API returns `401 invalid_api_key`.
- `perplexity` is not a registered provider in this checkout.

No `-deep-research-*.md` file was written, per CLAUDE.md (hand-written content must
never be named as a deep-research provider output).

## Gene identity

- UniProt: Q12908 (Ileal sodium/bile acid cotransporter; ASBT; IBAT; ISBT; NTCP2)
- 348 aa, 7 predicted transmembrane helices, glycoprotein; bile acid:sodium symporter
  (BASS, TC 2.A.28) family; InterPro IPR002657; PANTHER PTHR10361 (same family as
  SLC10A1/NTCP)
- Seven-TM topology was experimentally supported by glycosylation-scanning mutagenesis
  [PMID:15350125 "Membrane topology was further evaluated and confirmed by
  N-glycosylation-scanning mutagenesis, as reporter sites inserted in the putative
  extracellular loops 1 and 3 were glycosylated."]
- UniProt lists the subunit state as "Monomer and homodimer" and the subcellular
  location only as "Membrane; Multi-pass membrane protein" — i.e. UniProt itself does
  *not* record the apical restriction, which has to come from the literature (below).

## Core transport function

- Reabsorption of bile acids from the intestinal lumen is the defining role
  [PMID:7592981 "The ileal Na+/bile acid cotransporter plays a critical role in the
  reabsorption of bile acids from the small intestine."]
- Strictly Na+-dependent, Cl--independent taurocholate uptake on heterologous
  expression [PMID:9458785 "In transiently transfected COS cells, ileal Na(+)-bile acid
  cotransporter-mediated taurocholate uptake was strictly Na+ dependent and chloride
  independent."]
- Both conjugated and unconjugated bile acids are substrates [PMID:9458785 "Analysis of
  the substrate specificity in transfected COS or CHO cells showed that both conjugated
  and unconjugated bile acids are efficiently transported."]; UniProt curates Km values
  of 12–17 uM for taurocholate, 33–37 uM for cholate, and 2–6 uM for the glyco-
  conjugates.
- **Stoichiometry is 2 Na+ : 1 bile acid, and transport is electrogenic and
  bidirectional** — measured directly in voltage-clamped CHO cells expressing the human
  protein [PMID:9856990 "These results indicate that the cotransport of bile acids and
  Na+ by human apical sodium-bile acid transporter is electrogenic and bidirectional and
  is best explained by a 2:1 Na+:bile acid coupling stoichiometry."; "A 3-fold reduction
  in extracellular Na+ produced a negative 52 mV shift of the flux-voltage relationship,
  consistent with a 2:1 Na+:bile acid coupling stoichiometry."]. UniProt's curated RHEA
  reactions (RHEA:71875 etc.) likewise use 2 Na+. Note that the cached Reactome reaction
  R-HSA-194187 writes the reaction with a single sodium ion; the experimental literature
  and UniProt both say two.

## Apical / microvillar localization (the key family contrast)

This is the fact that distinguishes SLC10A2 from its sister SLC10A1 (NTCP), which is
basolateral in hepatocytes.

- [PMID:9856990 "Intestinal absorption of bile acids depends on a sodium-bile acid
  cotransport protein in the apical membrane of the ileal epithelial cell."]
- [PMID:33222321 "conjugated bile salts cross the otherwise impermeable lipid bilayer of
  (primarily terminal ileal) enterocytes through the apical sodium-dependent bile acid
  transporter (gene SLC10A2)"]
- [Reactome:R-HSA-194187 "In the body, ASBT is expressed on the apical surfaces of
  enterocytes, and this reaction is the first step in the process by which bile salts and
  acids are reaborbed from the intestinal lumen and returned to the liver"]
- The apical membrane of an ileal enterocyte *is* the microvillar (brush-border)
  membrane, which is why GO:0005902 microvillus and GO:0016324 apical plasma membrane
  are both annotated. The experimental grounding for both is on mouse Slc10a2
  (UniProtKB:P70172), which carries GO:0005902 and GO:0016324 by **IDA** (QuickGO);
  the human rows are Ensembl Compara transfers (GO_REF:0000107) from exactly that
  orthologue. No human-specific immunolocalization paper is present in the cache.

### PAINT confirms the apical/basolateral split at the node level

Donor tracing of the IBA rows (`SLC10A2-goa.tsv`; donor ids resolved via MGI, RGD and
UniProt):

| term | PTN node | donors |
|---|---|---|
| GO:0005886 plasma membrane | PTN000040759 | mouse Slc10a2 (MGI:1201406), rat Slc10a1 (RGD:3681), rat Slc10a2 (RGD:3682), human SLC10A1 (Q14973), human SLC10A4 (Q96EP9) |
| GO:0008508 bile acid:sodium symporter activity | PTN000040761 | rat Slc10a1, rat Slc10a2 |
| GO:0015721 bile acid and bile salt transport | PTN000040761 | rat Slc10a1, rat Slc10a2 |
| GO:0016324 apical plasma membrane | **PTN002570923** | mouse Slc10a2, rat Slc10a2 only |

So PAINT places plasma-membrane residence and Na+/bile-acid symport at ancestral SLC10
nodes shared by both branches, but places the **apical** location at a sub-node whose
donors are exclusively ASBT orthologues. The mirror-image node in the SLC10A1 review is
**PTN002570905**, which carries GO:0016323 basolateral plasma membrane with NTCP donors.
The apical/basolateral contrast asserted in the SLC10A1 review is therefore **confirmed
from the SLC10A2 side**, and it is explicitly represented in the phylogeny rather than
being an inference.

## Tissue distribution

- Ileum and kidney [PMID:9458785 "Using Northern blot analysis to determine its tissue
  expression, we readily detected the ileal Na(+)-bile acid cotransporter mRNA in
  terminal ileum and kidney."]; UniProt adds lower expression in cecum. The renal
  proximal-tubule role is a bile-acid salvage mechanism and is flagged "Probable" by
  UniProt.
- Also in biliary and colonic epithelium at lower levels [PMID:19498215 "In addition to
  the hepatocyte and enterocyte, subgroups of these bile acid transporters are expressed
  by the biliary, renal, and colonic epithelium where they contribute to maintaining
  bile acid homeostasis and play important cytoprotective roles."]

## Narrow substrate specificity (contrast with NTCP)

- [PMID:9458785 "Whereas the multispecific liver Na(+)-bile acid cotransporter may
  participate in hepatic clearance of organic anion metabolites and xenobiotics, the
  ileal and renal Na(+)-bile acid cotransporter retains a narrow specificity for
  reclamation of bile acids."]

This is the reason the SLC10A1 review's `GO:0042908 xenobiotic transport` replacement
term is **not** appropriate for SLC10A2: the same paper that justifies it for the liver
carrier explicitly denies the breadth for the ileal/renal one.

## Human loss of function

- P290S abolishes transport without affecting synthesis or trafficking
  [PMID:7592981 "In transfected COS-1 cells, the single amino acid change abolished
  taurocholate transport activity but did not alter the transporter's synthesis or
  subcellular distribution."] — a clean separation of transport activity from
  localization, and the model in PMID:15350125 rationalizes it as loss of bile-acid
  binding.
- Primary bile acid malabsorption (PBAM1, MIM:613291) is caused by SLC10A2 mutations
  [PMID:9109432 "These findings establish that SLC10A2 mutations can cause PBAM and
  underscore the ileal Na+/bile acid cotransporter's role in intestinal reclamation of
  bile acids."]; the L243P and T262M alleles reach the plasma membrane but cannot
  transport [PMID:9109432 "In transfected COS cells, the L243P, T262M, and double mutant
  (L243P/T262M) did not affect transporter protein expression or trafficking to the
  plasma membrane; however, transport of taurocholate and other bile acids was
  abolished."]
- The disease phenotype is itself the enterohepatic-circulation phenotype
  [PMID:9109432 "Primary bile acid malabsorption (PBAM) is an idiopathic intestinal
  disorder associated with congenital diarrhea, steatorrhea, interruption of the
  enterohepatic circulation of bile acids, and reduced plasma cholesterol levels."]
- ASBT is a validated drug target; ASBT inhibitors are in clinical use/trials for
  cholestatic pruritus and metabolic disease (PMID:33222321).

## Pathway position

- [PMID:19498215 "Following their movement with bile into the lumen of the small
  intestine, bile acids are almost quantitatively reclaimed in the ileum by the apical
  sodium-dependent bile acid transporter."]
- [Reactome:R-HSA-159418 "This recycling involves a series of transport processes: uptake
  by enterocytes mediated by ASBT (SLC10A2), traversal of the enterocyte cytosol mediated
  by ileal bile acid binding protein (I-BABP - FABP6), efflux from enterocytes mediated
  by MRP3 (ABCC3)"]
- UniProt: works with NTCP, OST-alpha/beta and BSEP for enterohepatic recycling
  (PubMed:33222321).

## Curation decisions and their reasoning

1. **12 `GO:0005515 protein binding` rows → REMOVE.** Ten are HuRI yeast-two-hybrid
   (PMID:32296183), one is BioPlex 3.0 affinity-purification MS (PMID:33961781 — the
   Huttlin *Cell* 2021 dual proteome-scale network paper, **not** a focused study of
   SLC10A2), one is the SLC-superfamily interactome survey (PMID:40355756). None assigns
   a molecular function. Per repo policy generic protein binding is removed as
   uninformative rather than marked over-annotated, and removal does not dispute the
   interactions. The two partners that recur are UPK1B, EFNA5, IFITM3, CTXN3, TTMP,
   NRM, CCL4L2, TMEM222, PSENEN, TEX264 (HuRI) and **CLPTM1 (O96005)** twice, from two
   independent methods; CLPTM1 is a putative lipid scramblase of the ER/Golgi membrane
   and is a frequent companion of membrane proteins in AP-MS, so the reproducibility
   does not by itself license a functional term. Raised in `suggested_questions`.
2. **Transport and localization rows → ACCEPT.** GO:0008508, GO:0015721, GO:0005886,
   GO:0016324, GO:0005902, GO:0016020. The PAINT node placements are all sound (table
   above) and the apical sub-node is correctly ASBT-restricted. GO:0016020 is a broad
   IEA parent of correctly annotated children and is kept.
3. **No `MODIFY` anywhere.** Every term in GOA for this gene is at the right
   granularity. In particular GO:0008508 is *not* obsolete (checked via OLS), and
   GO:0015125 bile acid transmembrane transporter activity would be an ancestor of
   GO:0008508, so adding it would be redundancy, not coverage.
4. **One `NEW` term: `GO:0098719 sodium ion import across plasma membrane`.**
   - *Participation.* ASBT itself translocates the Na+ ions. This is not a
     substrate/necessity argument: the human protein was voltage-clamped and shown to
     carry charge with a 2:1 Na+:bile acid stoichiometry [PMID:9856990], so the sodium
     leg of the symport is work the protein performs, in the same molecular event as the
     bile acid leg. Direction is import into the enterocyte, matching the term
     definition ("from outside of a cell, across the plasma membrane and into the
     cytosol", OLS).
   - *Comparator check (QuickGO, 2026-10-04).* Na+-coupled symporters conventionally
     carry a sodium-transport process term alongside their solute term: SLC5A1/SGLT1
     (P13866) has GO:0098719 by **IDA**; SLC34A1/NaPi-IIa (Q06495) has GO:0098719;
     SLC5A5/NIS (Q92911) has GO:0006814 sodium ion transport by IBA and GO:0035725 by
     IEA. So the term is conventionally applied to exactly this role. Within SLC10 it is
     absent from SLC10A2, SLC10A1 and mouse Slc10a2 alike — a family-level gap rather
     than a cross-family convention, which is the pattern that distinguishes a real
     omission from a convention I had not identified.
   - *Non-redundancy.* GO:0098719 is neither an ancestor nor a descendant of GO:0015721
     bile acid and bile salt transport.
   - *GO-CAM check.* `gocams/index.tsv` contains no model for SLC10A2 or Q12908, so no
     curator has already modelled this gene in a different role.
   - Chose the plasma-membrane-specific import term over the broader GO:0035725 because
     the location and direction are both experimentally established.
5. **No `NEW` process term for bile acid reclamation / enterohepatic circulation.**
   GO has no "enterohepatic circulation" term (OLS search returns nothing in GO), and
   GO:0015721 bile acid and bile salt transport already carries the transport claim at
   the right granularity. Inventing an intestinal-reabsorption process term was not
   pursued: the existing term plus the apical location already encode the reclamation
   step, and a more specific term would be a new-term request without a comparator set
   to anchor it. Raised in `suggested_questions` instead.

## Open items

- No GO-CAM model for SLC10A2 in `gocams/index.tsv` at review time; the Reactome
  reaction R-HSA-194187 is the only pathway-level representation, and its sodium
  stoichiometry (1 Na+) disagrees with the experimental 2:1.
- The renal proximal-tubule salvage role is "Probable" in UniProt and rests on mRNA
  detection in kidney [PMID:9458785] rather than on a transport assay in renal cells; no
  GO annotation asserts it and none was proposed.
- No human-specific microvillus/brush-border immunolocalization reference is cached; the
  localization rows rest on mouse IDA plus the human apical statements above.
