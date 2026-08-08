# RDH8 (human) — gene review notes

UniProt: Q9NYR8 (RDH8_HUMAN). HGNC:14423. Gene on chromosome 19.
Aliases: PRRDH (photoreceptor RDH), SDR28C2, "Short chain dehydrogenase/reductase family 28C member 2".

## Core identity / function

RDH8 is a **photoreceptor-outer-segment all-trans-retinol dehydrogenase** and a member of the
short-chain dehydrogenase/reductase (SDR) family.

- UniProt FUNCTION: "Retinol dehydrogenase with a clear preference for NADP. Converts all-trans-retinal
  to all-trans-retinol. May play a role in the regeneration of visual pigment at high light intensity
  (By similarity)." [file:human/RDH8/RDH8-uniprot.txt]
- EC 1.1.1.300; CATALYTIC ACTIVITY: "all-trans-retinol + NADP(+) = all-trans-retinal + NADPH + H(+)"
  (Rhea:RHEA:25033) [file:human/RDH8/RDH8-uniprot.txt]. Physiologically the enzyme runs in the
  **reductive** direction (all-trans-retinal -> all-trans-retinol) consuming NADPH.
- The reaction is exactly the definition of **GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity**
  ("Catalysis of the reaction: all-trans-retinol + NADP+ = all-trans-retinal + NADPH + H+.", QuickGO).
  This is the NADP-dependent term and is the best-supported MF, matching the EC and Rhea reaction
  in UniProt. GO:0004745 (NAD+ activity) is the NAD-form term; RDH8 has a "clear preference for NADP",
  so the NAD+ term is less appropriate (the IBA/TAS NAD+ annotations are the historical family term).

## Original characterization: PMID:10753906 (Rattner, Smallwood, Nathans 2000, J Biol Chem)

Abstract-only in cache (full_text_available: false). Key verbatim statements from the abstract
[PMID:10753906]:

- "Retinol dehydrogenase (RDH), the enzyme that catalyzes the reduction of all-trans-retinal to
  all-trans-retinol within the photoreceptor outer segment, was the first visual cycle enzymatic
  activity to be identified."
- "Previous work has shown that this enzyme utilizes NADPH, shows a marked preference for
  all-trans-retinal over 11-cis-retinal, and is tightly associated with the outer segment membrane."
- "This paper reports the identification of a novel member of the short chain dehydrogenase/reductase
  family, photoreceptor RDH (prRDH)..."
- "Bovine and human prRDH are highly homologous and are most closely related to
  17-beta-hydroxysteroid dehydrogenase 1."  <-- source of the InterPro/17beta-HSD-based over-annotations
- "protein blotting and immunocytochemistry show that prRDH localizes exclusively to both rod and cone
  outer segments and that prRDH is tightly associated with outer segment membranes."
- "Taken together, these data indicate that prRDH is the enzyme responsible for the reduction of
  all-trans-retinal to all-trans-retinol within the photoreceptor outer segment."

Note the abstract localizes prRDH to the **rod/cone outer segment membrane** ("tightly associated with
outer segment membranes"). It does NOT support cytosol (GO:0005829) or plasma membrane (GO:0005886) as
the specific site; GO:0001750 photoreceptor outer segment is the accurate compartment.

## Location

- UniProt SUBCELLULAR LOCATION: "Membrane; Multi-pass membrane protein." [file:human/RDH8/RDH8-uniprot.txt]
  Three predicted transmembrane helices (FT TRANSMEM 86..106, 137..157, 169..189).
- UniProt TISSUE SPECIFICITY: "Detected in photoreceptor outer segments in the retina (at protein level)."
  [file:human/RDH8/RDH8-uniprot.txt]
- HPA: "Tissue enriched (retina)." [file:human/RDH8/RDH8-uniprot.txt]
- So: an integral (multi-pass) membrane protein of the **photoreceptor outer segment**. The IBA "cytosol"
  and TAS "plasma membrane" annotations are inconsistent with a multi-pass membrane protein enriched in
  outer-segment membranes; GO:0016020 membrane (IEA/SubCell) and GO:0001750 photoreceptor outer segment
  are the accurate/specific locations.

## Cofactor

- UniProt BINDING 9..18 ligand NADP(+) (ChEBI:CHEBI:58349) [file:human/RDH8/RDH8-uniprot.txt].
  Rossmann-fold NAD(P)-binding domain (Gene3D 3.40.50.720). Supports **GO:0050661 NADP binding** as a
  core molecular function component.
- KW: NADP, Oxidoreductase. ACT_SITE 155 (Proton acceptor), catalytic Tyr/Lys of SDR.

## Visual-cycle context

- Reactome R-HSA-2453902 "The canonical retinoid cycle in rods (twilight vision)": RDH8 participates in
  the retinoid/visual cycle, reducing all-trans-retinal released from photobleached rhodopsin back to
  all-trans-retinol [file:human/RDH8/RDH8-uniprot.txt DR Reactome; reactome/R-HSA-2453902.md].
- This is the first (reductive) step of all-trans-retinal clearance from photoreceptors; protects
  against retinaldehyde toxicity and feeds retinol back toward the RPE for regeneration of 11-cis-retinal.
  Supports BP GO:0007601 visual perception, GO:0042572 retinol metabolic process, GO:0042574 retinal
  metabolic process.

## Disease

- UniProt DISEASE: Stargardt disease 5 (STGD5) [MIM:621259], autosomal recessive macular dystrophy,
  onset in the fifth decade. "The disease is caused by variants affecting the gene represented in this
  entry." [file:human/RDH8/RDH8-uniprot.txt] Ref: PMID:37628710 (Zampatti et al. 2023,
  "A Splicing Variant in RDH8 Is Associated with Autosomal Recessive Stargardt Macular Dystrophy",
  Genes (Basel) 14:1659). This confirms an in-vivo physiological role in the human visual cycle.

## Over-annotation analysis (steroid/estrogen)

The estradiol 17-beta-dehydrogenase [NAD(P)+] activity (GO:0004303), estrogen biosynthetic process
(GO:0006703), and steroid biosynthetic process (GO:0006694) annotations are all IEA (InterPro/ARBA)
or TAS derived from the family/homology relationship "most closely related to 17-beta-hydroxysteroid
dehydrogenase 1" [PMID:10753906]. RDH8's demonstrated substrate is all-trans-retinal/retinol; there is
no evidence RDH8 acts on estradiol/steroids in vivo. These are SDR-family (17beta-HSD1-based) domain
transfers, i.e. over-annotations / paralog-family inference, not RDH8's actual function.
- GO:0004303 (IEA, InterPro IPR011348 = "17beta_DH"): MARK_AS_OVER_ANNOTATED (InterPro domain-family
  transfer; RDH8 works on retinoids, not estradiol). Per policy, wrong-family IEA could be REMOVE,
  but the SDR fold genuinely is 17beta-HSD-like; conservative = MARK_AS_OVER_ANNOTATED.
- GO:0006703 estrogen biosynthetic process (IEA, InterPro): REMOVE candidate (clearly wrong BP from the
  same 17beta-HSD family transfer) — no evidence RDH8 is in estrogen biosynthesis.
- GO:0006694 steroid biosynthetic process: appears twice — IEA (ARBA GO_REF:0000117) and TAS
  (PMID:10753906, PINC). The TAS one is a legacy PINC assertion; the paper is about retinoid, not
  steroid, biosynthesis. MARK_AS_OVER_ANNOTATED for TAS (do not REMOVE a non-IEA legacy annotation);
  the IEA ARBA one is a machine over-annotation.

## Summary of core functions

1. MF: GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity (reductive direction: reduces
   all-trans-retinal to all-trans-retinol using NADPH). EC 1.1.1.300.
2. MF component: GO:0050661 NADP binding (Rossmann-fold cofactor binding).
3. BP: GO:0007601 visual perception / GO:0042572 retinol metabolic process (all-trans-retinal
   clearance/recycling in the visual cycle).
4. CC: GO:0001750 photoreceptor outer segment (integral multi-pass membrane protein of the outer segment).
</content>
