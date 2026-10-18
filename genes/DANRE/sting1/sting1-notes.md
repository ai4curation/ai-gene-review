# Zebrafish sting1 (STING/MITA, tmem173; ZFIN ZDB-GENE-120921-1; UniProt E7F4N7) — curation notes

## Provenance
Automated deep research (`just deep-research DANRE sting1 --provider perplexity`) was not usable in
this environment (no provider/agentapi available), so no `-deep-research-<provider>.md` file was
generated. These notes are compiled manually from the cached publications in `publications/` and the
UniProt record, with inline PMID provenance and verbatim supporting text.

## Summary of gene function
Zebrafish sting1 is the teleost ortholog of vertebrate STING (MITA/ERIS/MPYS/TMEM173), a 398-aa
multi-pass endoplasmic reticulum membrane adaptor of the cGAS-STING cytosolic nucleic-acid sensing
pathway. Unlike insect STING, **zebrafish possess a type I interferon system**, and zebrafish STING
drives both type I interferon (IFN) and NF-kappaB responses; a zebrafish-specific C-terminal-tail
motif biases its output strongly toward NF-kappaB. It also has a conserved, interferon-independent
role in autophagy induction.

### Signaling / interferon induction (core)
- zSTING is an ER adaptor orthologous to mammalian STING; overexpression constitutively induces IFN and
  ISGs and protects fish cells against RNA virus: [PMID:23091644 "overexpression of this ER protein in fish cells led to a constitutive\ninduction of IFN and interferon-stimulated genes (ISGs)."] and [PMID:23091644 "STING-overexpressing\ncells were almost fully protected against RNA virus infection with a strong\ninhibition of both DNA and RNA virus replication."]
- Works together with MAVS downstream of RIG-I in the IFN-inducing pathway: [PMID:23091644 "together with MAVS, STING was an important player in the RIG-I IFN-inducing\npathway."]
- Required for HSV-1 (DNA virus)-induced type I IFN in zebrafish larvae; cGAS is dispensable, DDX41/DHX9 act as sensors: [PMID:25972544 "HSV-1 infection triggers strong\ntype I interferon production, which depends on STING expression."] and [PMID:25972544 "Silencing of zSTING, but not zMAVS, markedly\nattenuates the DNA virus-induced antiviral responses."]
- DrDDX41 signals through DrSTING to activate NF-kappaB and IFN pathways and antibacterial immunity: [PMID:29942316 "DrDDX41 acts as an initiator for the activation of NF-κB and IFN signaling pathways in a\nDanio rerio STING (DrSTING)-dependent manner"] and [PMID:29942316 "knockdown of either DrDDX41 or DrSTING/DrSTAT6\nsignificantly reduced the survival of zebrafish under Aeromonas hydrophilia or\nEdwardsiella tarda infection."]
- DrcGAS homologs activate NF-kappaB and IFN-I in a STING-dependent manner; knockdown reduces immunity to bacteria and viruses: [PMID:32285982 "Overexpression of DrcGASa/b in HEK293T cells and zebrafish embryos significantly\nactivated NF-κB and IFN-I signaling pathways in a STING-dependent manner."]

### C-terminal tail / NF-kappaB bias and TRAF6 recruitment
- A motif appended to the zebrafish STING CTT inverts the vertebrate signaling response toward strong NF-kappaB and weak IRF3-IFN, by recruiting TRAF6: [PMID:31018131 "a motif appended to the\nCTT of zebrafish STING that inverts the typical vertebrate signaling response\nand results in dramatic NF-κB activation and weak IRF3-interferon signaling."] and [PMID:31018131 "co-crystal structure that explains how this CTT sequence recruits\nTRAF6 as a new binding partner"]
- This grounds treating the IPI "protein binding" (partner traf6, ZFIN:ZDB-GENE-030131-5735) as a molecular adaptor / signaling-hub activity rather than an uninformative binding term: [PMID:31018131 "our results define the STING CTT as a linear signaling hub"]

### Autophagy (interferon-independent, conserved)
- STING activates autophagy independently of TBK1/IFN; zebrafish (dr) STING was among the orthologs tested for cGAMP-induced LC3 conversion: [PMID:30842662 "STING also activates autophagy through a mechanism that\nis independent of TBK1 activation and interferon induction."]
- In zebrafish, DRAM1-mediated selective autophagic defense against mycobacteria requires STING: [PMID:24922577 "DRAM1-mediated selective autophagic defenses require\nthe cytosolic DNA sensor STING and the selective autophagy receptor p62/SQSTM1."]

### Localization
- Endoplasmic reticulum / ER membrane (experimental in zebrafish): [PMID:23091644 "an endoplasmic reticulum (ER)\nadaptor: the stimulator of interferon genes (STING) protein"]. UniProt (by similarity to human Q86WV6) additionally places it at the ERGIC membrane, Golgi membrane, perinuclear region and autophagosome membrane, reflecting the conserved STING trafficking itinerary.

### Ligand binding and proton-channel activity (by similarity)
- Binds cyclic dinucleotides (c-di-GMP, 2'3'-cGAMP; UniProt binding-site features by similarity to Q86WV6). 
- Proton channel activity / proton transmembrane transport are transferred by similarity (ISS) from mammalian STING, where proton-channel activity from the Golgi drives LC3 lipidation for autophagy.

## Curation implications
- In contrast to Drosophila Sting, the type I interferon annotations (GO:0032479, GO:0032481) are
  biologically appropriate for zebrafish, which has a functional IFN system and whose STING drives IFN.
- The autophagosome / reticulophagy / autophagosome-membrane terms are inherited (IBA/IEA/ISS) from the
  conserved STING autophagy function; retained as non-core where inherited, but the autophagy-regulation
  process terms with experimental (IDA/IGI) support are accepted.
- The IPI GO:0005515 protein binding (partner traf6) is uninformative as-is but the cited structure
  supports a molecular adaptor / signaling-hub activity, so it is modified to molecular adaptor activity.
- Core functions: cGAS/STING signaling adaptor at the ER membrane driving type I interferon and NF-kappaB
  antiviral/antibacterial responses, cyclic-dinucleotide binding, and autophagy induction.
