# SLC10A1 (NTCP) curation notes

## Provenance of this review

Automated deep research was attempted and **failed for both configured providers**, so
the literature synthesis below was assembled by hand from the cached publications in
`publications/` plus the UniProt record:

- `just deep-research-falcon human SLC10A1 --fallback perplexity-lite` →
  Edison/Falcon API returned `402 Payment Required`; `perplexity-lite` is not a
  registered provider in this checkout (available: openai, falcon, openscientist).
- `just deep-research-openai human SLC10A1` → OpenAI API returned
  `401 invalid_api_key`.

No `-deep-research-*.md` file was written (per CLAUDE.md, hand-written content must
never be named as a deep-research provider output).

## Gene identity

- UniProt: Q14973 (Hepatic sodium/bile acid cotransporter; NTCP; GIG29)
- Family: bile acid:sodium symporter (BASS); PANTHER PTHR10361; InterPro IPR002657,
  IPR004710
- 349 aa, glycosylated, multi-pass membrane protein; gene on chromosome 14
  [PMID:8132774 "Southern blot analysis of genomic DNA from a panel of human/hamster
  somatic cell hybrids mapped the human NTCP gene to chromosome 14."]

## Core transport function

- Na+-dependent taurocholate uptake on heterologous expression, high affinity
  [PMID:8132774 "Saturation kinetics indicated that the human NTCP has a higher affinity
  for taurocholate (apparent Km = 6 microM) than the previously cloned rat protein
  (apparent Km = 25 microM)."]
- Main hepatic bile salt uptake system [PMID:35545671 "Human Na+-taurocholate
  co-transporting polypeptide (NTCP) is the main bile salt uptake system in liver."]
- Gated-pore mechanism resolved by cryo-EM [PMID:35545671 "NTCP undergoes a
  conformational transition opening a wide transmembrane pore that serves as the
  transport pathway for bile salts, and exposes key determinant residues for HBV/HDV
  binding to the outside of the cell."]
- Basolateral hepatocyte localization and drug transport [PMID:34060352 "The
  Na+/taurocholate cotransporting polypeptide (NTCP) is located in the basolateral
  membrane of hepatocytes, where it transports bile acids from the portal blood back into
  hepatocytes."]
- 2 Na+ per bile salt, per the curated reaction set in UniProt (RHEA:71875 and relatives)
  and [Reactome:R-HSA-194121 "A molecule of extracellular bile salt (glyco- or
  taurocholate, or glyco- or taurochenodeoxycholate) and two sodium ions are transported
  into the cytosol, mediated by NTCP (Na+ / taurocholate cotransporter) in the plasma
  membrane."]

## Substrate breadth (bile salts and beyond)

- Multispecific relative to the ileal transporter [PMID:9458785 "Whereas the
  multispecific liver Na(+)-bile acid cotransporter may participate in hepatic clearance
  of organic anion metabolites and xenobiotics, the ileal and renal Na(+)-bile acid
  cotransporter retains a narrow specificity for reclamation of bile acids."]
- Bile acid and estrone sulfate recognition are genetically separable
  [PMID:14660639 "exhibited a near complete loss of function for bile acid uptake yet
  fully normal transport function for the non-bile acid substrate estrone sulfate"]
- Rosuvastatin is a substrate; cyclosporine A, benzbromarone, MK571 and fluvastatin
  inhibit (PMID:34060352).

## Oligomeric state

- Dimers persist at the plasma membrane [PMID:22029531 "FRET (fluorescence resonance
  energy transfer) using fluorescently labelled subunits further demonstrated that
  dimerization persists at the plasma membrane."]
- Subunits are independently functional [PMID:22029531 "In conclusion, NTCP adopts a
  dimeric structure in which individual subunits are functional."]
- Heteromers with SLC10A4/SLC10A6 form and can reduce surface delivery
  [PMID:22029531 "SLC10A4 and SLC10A6 co-immunoprecipitated with NTCP, demonstrating that
  heteromeric complexes can be formed between SLC10A family members in vitro."]

## Human loss of function

- NTCP deficiency: extreme conjugated hypercholanemia, mild phenotype, bile salt
  synthesis and FGF19 signalling intact; mutant protein mislocalized
  [PMID:24867799 "Immunofluorescence studies and surface biotinylation experiments
  demonstrated that the mutant protein is virtually absent from the plasma membrane."]
- Pathway context and population frequency of NTCP deficiency in PMID:33222321.

## HBV/HDV receptor function

- [PMID:23150796 "Silencing NTCP inhibited HBV and HDV infection, while exogenous NTCP
  expression rendered nonsusceptible hepatocarcinoma cells susceptible to these viral
  infections."] Humanizing residues 157-165 of the monkey orthologue is sufficient to
  support infection.
- Structural basis in PMID:35545671, PMID:35580629, PMID:35580630.

## Curation decisions and their reasoning

1. **87 + 1 `GO:0005515 protein binding` rows → REMOVE.** All come from two systematic
   interaction surveys (HuRI, PMID:32296183; SLC interactome, PMID:40355756) that assign
   no function. Per repo policy, generic protein binding is removed as uninformative
   rather than marked over-annotated, and removal does not dispute the interactions.
2. **Transport and localization rows → ACCEPT** (GO:0008508, GO:0015125, GO:0015721,
   GO:0005886, GO:0016323, GO:0016020). The IBA node placements are sound: the
   NTCP/ASBT clade shares Na+-dependent bile acid symport, and the NTCP-specific
   sub-node (PANTHER:PTN002570905) is correctly basolateral, unlike the apical ileal
   ASBT branch. GO:0016020 is a broad IEA parent of correctly annotated children and is
   kept.
3. **`GO:0031667 response to nutrient levels`, `GO:0043627 response to estrogen`,
   `GO:0045471 response to ethanol` → REMOVE.** All three are GO_REF:0000107 transfers
   from rat Ntcp (UniProtKB:P26435) where the underlying observation is modulation of
   transporter expression/activity. Being regulated by a stimulus is not participating in
   the response to it; NTCP performs no step of nutrient sensing, estrogen signalling or
   ethanol metabolism. NTCP deficiency leaves bile salt synthesis and intestinal FGF19
   signalling intact (PMID:24867799), i.e. no evidence that NTCP acts within such
   responses. Note that estrone-3-sulfate transport is a substrate relationship, whose
   proper representation is a transporter activity term, not "response to estrogen".
4. **`GO:0071466 cellular response to xenobiotic stimulus` → MODIFY → `GO:0042908
   xenobiotic transport`.** Here there *is* a real activity, not just a regulatory
   effect: the liver carrier is explicitly described as multispecific and as
   participating in hepatic clearance of xenobiotics (PMID:9458785), and human NTCP
   transports rosuvastatin (PMID:34060352). But what the protein does is transport the
   xenobiotic, not respond to it. (GO:0015711 organic anion transport and GO:0008514
   organic anion transmembrane transporter activity are both obsolete — checked via OLS
   — so the xenobiotic transport term is the available fit.)
5. **Two `NEW` annotations: `GO:0001618 virus receptor activity` and `GO:0046718
   symbiont entry into host cell`.** Absent from GOA for Q14973 (checked via QuickGO),
   despite being one of the best-characterized facts about the human protein.
   - Participation test: NTCP itself does the receptor work — direct preS1
     cross-linking, and necessity *and* sufficiency in cell culture (PMID:23150796) —
     and the transporter's conformational state governs preS1 exposure (PMID:35545671).
   - Comparator check: ACE2 (Q9BYF1) and CD4 (P01730), both host proteins with their own
     enzymatic/immune function serving as entry receptors, carry GO:0001618 and
     GO:0046718 by IDA (QuickGO query). So the terms are conventionally applied to this
     exact role; their absence on SLC10A1 is a gap, not a convention.

## Open items

- No GO-CAM model for SLC10A1 was found in `gocams/index.tsv` at review time.
- Whether the obsoletion of the organic-anion transport terms leaves estrone-3-sulfate
  uptake without a representable activity term is raised in `suggested_questions`.
