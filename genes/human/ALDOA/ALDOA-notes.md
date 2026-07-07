# ALDOA (P04075) — curation notes

Human fructose-bisphosphate aldolase A (muscle/red-cell isozyme). HGNC:414, chromosome 16, 364 aa.
Deep research: falcon OUT OF CREDITS (HTTP 402) — no `-deep-research-falcon.md`. Review grounded in
`ALDOA-uniprot.txt`, seeded GOA, and cached `publications/PMID_*.md`.

## Core biology

- Class-I fructose-bisphosphate aldolase; homotetramer; Schiff-base (lysine) mechanism
  [file:human/ALDOA/ALDOA-uniprot.txt "Belongs to the class I fructose-bisphosphate aldolase family";
   "Schiff-base intermediate with dihydroxyacetone-P" (ACT_SITE 230); KW "Schiff base"].
- Reversible aldol cleavage of beta-D-fructose 1,6-bisphosphate -> dihydroxyacetone phosphate (DHAP)
  + D-glyceraldehyde 3-phosphate (G3P); EC 4.1.2.13; RHEA:14729
  [file:human/ALDOA/ALDOA-uniprot.txt "beta-D-fructose 1,6-bisphosphate = D-glyceraldehyde 3-phosphate + dihydroxyacetone phosphate"].
- Fourth step of glycolysis (step 4/4 to make triose phosphates); reverse aldol condensation in gluconeogenesis
  [file:human/ALDOA/ALDOA-uniprot.txt "plays a key role in glycolysis and gluconeogenesis"; PATHWAY "glycolysis; ... step 4/4"].
- Kinetics: KM ~52 uM (30C) or 24 uM for F1,6BP [PMID:14766013; PMID:2204832].
- Structures solved (1ALD, 5KY6, 6XMH etc.); C-terminal region flexibility governs substrate entry/release
  [PMID:14766013 abstract; PMID:10048322 abstract].
- Three vertebrate isozymes: A (muscle), B (liver), C (brain)
  [file:human/ALDOA/ALDOA-uniprot.txt "aldolase A in muscle, aldolase B in liver and aldolase C in brain"].
  Paralog ALDOB already reviewed (fructolysis). Shared PANTHER PTHR11627.
- Tissue: HPA "Group enriched (skeletal muscle, tongue)"; abundant in RBC and muscle.

## Disease

- Glycogen storage disease 12 (GSD12) / ALDOA deficiency [MIM:611881]: hereditary nonspherocytic
  hemolytic anemia, myopathy with exercise intolerance and rhabdomyolysis (often febrile-triggered).
  [file:human/ALDOA/ALDOA-uniprot.txt "hemolytic anemia. It may lead to myopathy with exercise intolerance and rhabdomyolysis"].
  Patient variants: Arg303X/Cys338Tyr compound het (severe: anemia + rhabdomyolysis, death age 4)
  [PMID:14615364 "Hemolytic anemia and severe rhabdomyolysis caused by compound heterozygous mutations"];
  Glu206Lys, Gly346Ser, etc [PMID:14766013].

## Moonlighting (real but non-core)

- Actin/cytoskeleton binding: all 3 isozymes bind actin-containing filaments; aldolase A binds skeletal-muscle
  cytoskeleton most tightly; binding inhibited by F1,6BP and F1P; reversibly regulates cell contraction / stress fibers.
  [PMID:9244396 "bound more tightly to the skeletal muscle cytoskeleton"; "aldolase A associated with the cytoskeleton";
   "reversibly inhibited the contraction of MRC-5 cells"].
- F-actin paracrystal formation [PMID:1008835].
- WASP (Wiskott-Aldrich syndrome protein) binding via hydrophobic active-site pocket; competitive with substrate
  and actin/cortactin; "aldolase exists in distinct forms that regulate glycolysis or actin dynamics" [PMID:17329259].
  (Note: 17329259 also cited for tubulin binding GO:0015631 but paper is about WASP/actin, not tubulin — see MODIFY.)
- RNA binding: mRNA-interactome capture hit [PMID:22681889].
- Cadherin binding: E-cadherin BioID proximity proteomics hit [PMID:25468996].
- Insulin secretion via MRGPRE-beta-arrestin-1-ALDOA signaling [PMID:40446798] — pancreatic/glucose-homeostasis role.
- Sperm head localization / zona-pellucida binding [PMID:23355646] — moonlighting per authors.
- FBP2 (muscle fructose-1,6-bisphosphatase) interaction [PMID:18214967].
- Sub-localizations in high-throughput proteomics: extracellular exosome (many PMIDs), extracellular region,
  membrane, nucleus, granule lumen (Reactome degranulation). These are HDA/TAS bystander detections, non-core.

## Key GO decisions

- Core MF: GO:0004332 fructose-bisphosphate aldolase activity (EXP/IDA/IBA/IEA) — ACCEPT.
- Core BP: GO:0006096 glycolytic process, GO:0061621 canonical glycolysis, GO:0030388 F1,6BP metabolic process,
  GO:0006000 fructose metabolic process — ACCEPT (glycolysis) / KEEP context; GO:0006094 gluconeogenesis ACCEPT.
- Core CC: GO:0005829 cytosol — ACCEPT.
- fructose binding GO:0070061 — ACCEPT (substrate binding, IDA + IEA).
- Moonlighting MF/BP/CC treated KEEP_AS_NON_CORE (actin/cytoskeleton/tubulin/RNA/cadherin binding; muscle contraction,
  cell shape, actin filament org, insulin secretion, sperm-ZP binding, sperm head, I/M band, exosome/membrane/nucleus).
- protein binding GO:0005515 IPIs (many) — bare protein binding; MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).
- tubulin binding GO:0015631 TAS PMID:17329259 — paper is WASP/actin, not tubulin; MODIFY toward actin/WASP context or
  MARK_AS_OVER_ANNOTATED. Chose MARK_AS_OVER_ANNOTATED (tubulin binding not supported by that ref's abstract).
- ATP biosynthetic process GO:0006754 IMP PMID:14615364 — indirect (glycolytic ATP via deficiency phenotype);
  KEEP_AS_NON_CORE (downstream/indirect, defer to curator's full-text IMP).
- protein homotetramerization GO:0051289 ISS — ACCEPT as non-core (structural; homotetramer well documented).
</content>
</invoke>
