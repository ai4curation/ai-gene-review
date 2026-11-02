# Cdc42 (rat, UniProt Q8CFN2): manual literature synthesis

No deep-research provider was available for this session. This synthesis was written by the
reviewer from the cached publications in `publications/`, the UniProt record
(`Cdc42-uniprot.txt`) and the cached Reactome entry. Every claim carries its provenance.
Papers marked (abstract only) have no full text in the cache.

## Identity and family

- Rat Cdc42 (RGD:71043, GeneID 64465) is a 191-residue Rho-family small GTPase; the mature
  chain (1-188) carries a C-terminal S-geranylgeranyl cysteine and methyl ester, with residues
  189-191 removed [UniProtKB:Q8CFN2 "Belongs to the small GTPase superfamily. Rho family. CDC42
  subfamily."]. Two splice isoforms differ only in the last ten residues ("PKKSRRCVLL ->
  TQPKRKCCIF (in isoform 2)") [UniProtKB:Q8CFN2].
- Domain signatures: InterPro IPR037874 Cdc42, IPR003578 Small_GTPase_Rho, Pfam PF00071, PROSITE
  PS51420 RHO; PANTHER PTHR24072 (Rho family GTPase) [UniProtKB:Q8CFN2].

## Molecular function: a GTP/GDP switch

- Intrinsic GTP hydrolysis (EC 3.6.5.2, RHEA:19669) is recorded with experimental evidence from
  PMID:25498153 [UniProtKB:Q8CFN2 "Reaction=GTP + H2O = GDP + phosphate + H(+)"]. In that paper
  ArhGAP44 accelerated hydrolysis of GTP-Cdc42 in pulldown assays [PMID:25498153 "GTPase
  pull-down assay show hydrolysis of GTP-Cdc42 (green) and GTP-Rac1 (red) by ArhGAP44."].
- Regulation follows the canonical Rho cycle: GEFs, GAPs and GDIs [UniProtKB:Q8CFN2 "Regulated by
  guanine nucleotide exchange factors (GEFs) which promote the exchange of bound GDP for free
  GTP"].
- RhoGDIalpha binds Cdc42 from rat embryo fibroblast lysates; Ser34 phosphorylation of the GDI
  selectively releases RhoA but not Cdc42 [PMID:20472934 "Here, it is demonstrated that
  conventional PKC phosphorylates RhoGDIalpha on serine 34, resulting in a specific decrease in
  affinity for RhoA but not Rac1 or Cdc42."; "When Ser-34 was mutated to Asp, there was
  significantly reduced RhoGDIα binding to RhoA (by around 75%) but not Rac1 or Cdc42."].
- Effector engagement: GTP-Cdc42 activates N-WASP and thereby the Arp2/3 complex; Reactome
  describes the assay with rat Cdc42 [Reactome:R-NUL-442561 "The binding of the ARP2/3 complex to
  CDC42:GTP-activated N-WASP was demonstrated using rat Cdc42 and N-Wasp"]. Cdc42 binds the
  coatomer coat on Golgi membranes and acts through N-WASP and Arp2/3 there [PMID:15147909
  (abstract only) "Actin dynamics at the Golgi are regulated in part by recruiting Cdc42 or Rac
  to the membrane through a binding interaction with the coatomer-coated (COPI)-vesicle coat
  protein, coatomer."]. Cdc42 forms a complex with MLK3 in ischemic rat hippocampus
  [PMID:17161586 (abstract only) "enhanced assembly of the Cdc42-MLK3 complex"]. VAMP2 binds
  Cdc42 directly [PMID:15537656 (abstract only) "In vitro binding analyses showed that VAMP2 bound
  directly to Cdc42"].

## Cellular roles shown in rat cells or tissue

- Cell polarity: in primary rat astrocytes Cdc42, through Par6-PKCzeta, controls GSK-3beta and
  APC to polarize the centrosome and protrusion [PMID:12610628 (abstract only) "We conclude that
  Cdc42 regulates cell polarity through the spatial regulation of GSK-3beta and Apc."].
- Actin protrusion: in rat MTLn3 carcinoma cells EGF activates Cdc42 at the protruding edge and
  Cdc42 knockdown reduces barbed ends, Arp2/3 recruitment and actin branching [PMID:17855387
  (abstract only) "a marked defect in actin filament branching, as revealed by rotary-shadowing
  scanning electron microscopy"].
- Cytokinesis: in NRK cells Cdc42 depletion does not block cytokinesis but loosens equatorial
  actin and RhoA [PMID:21763307 "Our results indicate that Cdc42 activity per se is dispensable
  for cytokinesis in NRK cells, similar to what was seen in fibroblastid cells [18]."; "In
  contrast to previous observations in HeLa cells [17], no apparent defects were found in
  chromosome congression and separation in cells depleted of Cdc42"].
- Golgi positioning: ARHGAP21-regulated Cdc42 on Golgi membranes restrains dynein-driven Golgi
  motility in NRK cells and on rat liver Golgi membranes [PMID:20525016 "Together, our results
  reveal that dynein and microtubule-dependent Golgi positioning is regulated by ARF1-,
  coatomer-, and ARHGAP21-dependent Cdc42 signaling."].
- Dendritic spine plasticity: in CA1 neurons of rat hippocampal slices Cdc42 is activated within
  the single stimulated spine downstream of NMDA receptor/CaMKII and is required for the
  sustained phase of spine enlargement [PMID:21423166 "Thus, RhoA and Cdc42 relay transient
  CaMKII activation to synapse-specific, long-term signalling required for spine structural
  plasticity."].
- Insulin exocytosis (mouse MIN6 cells): glucose activates Cdc42 and Cdc42-VAMP2 moves from the
  granule fraction to the plasma membrane [PMID:15537656 (abstract only)].
- Angiogenic sprouting of rat skeletal-muscle microvascular endothelial cells: Cdc42QL increased
  and Cdc42N17 decreased sprouting; active Cdc42 lowered RhoA activity [PMID:18562481 (abstract
  only) "Activation of Cdc42 was sufficient to decrease RhoA activity."].
- JNK signalling: dominant-negative Cdc42N17 blunts agonist-induced JNK1 activation and DNA
  synthesis in rat hepatocytes [PMID:9487126 "These data suggest that HGF signaling progresses
  via Rac1 to Cdc42 and then to the JNK/SAP kinase cascade in hepatocytes."]; Cdc42 knockdown
  suppresses MLK3/MKK7/JNK3 signalling and neuronal death after ischemia [PMID:17161586].
- NPC1L1 trafficking: GTP-Cdc42 binds NPC1L1 and is needed for its transport from the endocytic
  recycling compartment to the plasma membrane [PMID:21844200 (abstract only)].
- Expression in developing rat submandibular gland, associated with lumen formation and
  polarization [PMID:18784978 (abstract only)].

## Summary

Rat Cdc42 is the canonical Cdc42 orthologue. Its molecular function is that of a membrane-anchored
GTP/GDP switch (G protein activity, with intrinsic GTPase activity) that binds GBD/CRIB-containing
effectors (N-WASP, PAKs, MLK3, Par6) when GTP-bound and RhoGDI when GDP-bound. The best-supported
cellular outputs are actin filament organization and protrusion (filopodia, lamellipodia, Arp2/3
branching), establishment of cell polarity, Golgi positioning and the maintenance of dendritic
spine structural plasticity. The developmental and organ-level processes in GOA are inherited
by orthology from mouse knockouts and record necessity rather than steps that Cdc42 performs.
