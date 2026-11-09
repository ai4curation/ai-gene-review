# fruA review notes

## Evidence synthesis

- fruA encodes the membrane EIIB'BC component of the E. coli fructose PTS. Prior
  and Kornberg cloned the complete 1689 bp fruA ORF and showed that a plasmid
  carrying fruA+ alone restored fructose growth and fructose phosphorylation to
  fruA mutants. The cached abstract also explicitly describes Enzyme IIfru as
  the PEP-dependent PTS enzyme that couples fructose uptake to fructose
  1-phosphate formation [PMID:3076173].
- Charbit, Reizer, and Saier dissected the N-terminal duplicated EIIB' domain.
  Deleting EIIB' impaired low-fructose transport in vivo and lowered affinity
  for FruB/DTP in vitro, while C112S in the catalytic EIIB domain made FruA
  inactive as both a phosphoryl carrier and a sugar transport protein
  [PMID:8626640].
- PMID:8626640 also supports oligomeric FruA function, because mutant FruBC
  could inhibit detergent-solubilized wild-type or FruBC enzyme and the authors
  interpreted the functional permease as an oligomer requiring active IIB
  domains.
- The 2019 PTS membrane-interaction study confirms FruA interactions with FruB
  and several other PTS permeases, but the interaction row seeded by EcoCyc is
  only GO:0005515 protein binding. There is no specific replacement MF that can
  be inferred safely from those interactions alone [PMID:31751341].

## Curation decisions

- GO:0022877 and GO:0090582 both describe exact fructose-specific facets of the
  FruA PTS transporter step. GO:0022877 captures the overall FruB
  phosphohistidine-to-fructose group-translocation reaction used by the module
  annoton, while GO:0090582 captures the EIIB phosphocysteine-to-D-fructose
  half-reaction tested by the C112S mutant.
- GO:0009401 is broad relative to GO:1990539 fructose import across plasma
  membrane, but it is still correct. FruA is not merely upstream of the PTS; it
  is the EIIB'BC Enzyme II component that executes the membrane group
  translocation/phosphorylation step.
- GO:0005351 carbohydrate:proton symporter activity appears to be an
  over-broad or mechanistically wrong InterPro2GO mapping on the fructose EIIC
  domain. E. coli FruA is PEP/phosphorelay driven, and the GO:1902600 proton
  transmembrane transport row is only a logical consequence of that unsupported
  MF.
- The generic GO:0016020 membrane annotation is true but less specific than
  plasma membrane. The broad GO:1902495 transmembrane transporter complex row
  is compatible with FruA oligomerization, but no fructose-Enzyme-II-specific
  GO complex term exists in the seeded annotations.

## 2026-11-05 completion pass (Claude (AI-assisted))

- GO:0016020 membrane changed from KEEP_AS_NON_CORE to MODIFY -> GO:0005886
  plasma membrane: the term is correct but general, and the gene already
  carries the specific term (IDA PMID:15919996, PMID:17309111). Added the
  curated UniProt inner-membrane statement (ECO:0000269 PubMed:15919996).
- Core MF: GO:0022877 is kept as the primary core activity, matching the
  UniProt catalytic activity RHEA:49252 (EC 2.7.1.202) curated with
  ECO:0000269 from PMID:8626640. GO:0090582 (IMP, C112S) is kept as the second
  core activity for the EIIB phosphocysteine-to-fructose half-reaction; the two
  terms are not is_a related, so neither row is a MODIFY of the other.
- Deep research: the perplexity provider is not available in this environment
  (the same command failed for PSEPK fruA); no provider file was created.
- No PENDING/UNDECIDED rows remain; status set to COMPLETE.
