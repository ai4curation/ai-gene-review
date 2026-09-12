# DNAJC9 (HDJC9 / DnaJ protein SB73) research notes

## Identity
- UniProt Q8WXX5 (DNJC9_HUMAN), 260 aa. HGNC:19123. Type C DnaJ/HSP40.
- Domain: N-terminal J domain (15..82, HPD motif at 43-45); C-terminal histone-binding region (171..249,
  solved by X-ray in complex with MCM2 + H3.3-H4) [file:human/DNAJC9/DNAJC9-uniprot.txt FT DOMAIN J / REGION].

## Dual function (the key point)
- DNAJC9 is a DUAL histone chaperone AND HSP70 heat-shock co-chaperone.
  [PMID:33857403 "we identify and characterize a histone chaperone function of DNAJC9, a heat shock
  co-chaperone that promotes HSP70-mediated catalysis."]
- It forms a co-chaperone complex with MCM2 and histone H3-H4 heterodimers and recruits HSP70 via its J
  domain to fold H3-H4. [PMID:33857403 "We elucidate the structure of DNAJC9, in a histone H3-H4
  co-chaperone complex with MCM2, revealing how this dual histone and heat shock co-chaperone binds
  histone substrates. We show that DNAJC9 recruits HSP70-type enzymes via its J domain to fold histone
  H3-H4 substrates"]
- Integrates ATP-resourced folding into the histone supply pathway, during replication- and
  transcription-coupled nucleosome assembly. [PMID:33857403 "DNAJC9 integrates ATP-resourced protein
  folding into the histone supply pathway to resolve aberrant intermediates throughout the dynamic lives
  of histones."]
- UniProt FUNCTION: "Acts as a dual histone chaperone and heat shock co-chaperone... forms a co-chaperone
  complex with MCM2 and histone H3-H4 heterodimers... may recruit histone chaperones ASF1A, NASP and SPT2
  to histone H3-H4 heterodimers... Also plays a role as co-chaperone of the HSP70 family... Exhibits
  activity to assemble histones onto DNA in vitro." [file:human/DNAJC9/DNAJC9-uniprot.txt]

## HSP70 co-chaperone activity (original characterization)
- [PMID:17182002 "HDJC9 can interact with HSP70s and activate the ATPase activity of HSP70s, both of which
  are dependent on the J domain. Our data suggest that HDJC9 is a novel cochaperone for HSP70s."]
- J-domain stimulates HSP70 ATPase = ATPase activator activity (GO:0001671). GOA records this as
  GO:0032781 positive regulation of ATP-dependent activity (IDA PMID:17182002) and GO:0031072 HSP binding.

## Localization
- Predominantly NUCLEAR under normal conditions; translocates to cytoplasm and plasma membrane after heat
  shock via a non-classical lipid-dependent pathway. [PMID:17182002 "HDJC9 is mainly localized in cell
  nuclei under normal culture conditions while it is transported into cytoplasm and plasma membrane upon
  heat shock stress through a non-classical and lipid-dependent pathway."]
- Plasma membrane / extracellular region (IDA PMID:17182002) reflect the heat-shock translocation, a
  specialized/stress context -> KEEP_AS_NON_CORE.

## GOA WITH-partner key
- P68431=H3 (H3C12), Q6NXT2=H3-5, Q8NDC4=MORN4, P49736=MCM2, P62805=H4, P84243=H3.3, Q71DI3=H3.2,
  P0DMV9=HSPA1B, P0DMV8=HSPA1A, P11142=HSPA8, P34931=HSPA1L.

## Review logic
- histone binding (GO:0042393, IDA): ACCEPT, CORE.
- heat shock protein binding (GO:0031072, IBA + IPI): ACCEPT, CORE (binds HSP70).
- protein-folding chaperone binding (GO:0051087, IDA): ACCEPT (binds MCM2/HSP70 chaperone partners).
- positive regulation of ATP-dependent activity (GO:0032781, IDA): ACCEPT — J domain stimulates HSP70 ATPase.
- nucleosome assembly (GO:0006334, IDA): ACCEPT, CORE BP.
- protein folding chaperone complex (GO:0101031, IDA part_of): ACCEPT.
- nucleus (IBA/IEA/IDA): ACCEPT (predominant). cytoplasm (IBA/IEA/IDA): KEEP_AS_NON_CORE (heat-shock relocalization).
- plasma membrane / extracellular region: KEEP_AS_NON_CORE (stress-induced translocation).
- protein binding (GO:0005515, IPI x several): bare term; histone partners -> some better captured by
  histone binding, but per guidelines KEEP_AS_NON_CORE for the bare-term rows.
