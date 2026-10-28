# FLNA source and context guide
The review preserves 150 genuine seed rows covering 151 TSV rows and all 152 original QuickGO contexts. Stored decisions are 25 ACCEPT, 111 KEEP_AS_NON_CORE, 7 UNDECIDED, 2 MARK_AS_OVER_ANNOTATED and 5 TOO_GENERAL. Original-context counts are 26, 112, 7, 2 and 5 respectively. There are three unchanged natural products, one core, and no NEW annotations or supporting-text quotations. [Evidence synthesis](FLNA-source-evidence.md) records biological and access boundaries.
## Deterministic projection
Two source collapses are retained rather than repaired by hand. The source TSV and seeded machine fields are not edited. The original JSON contexts remain in the reproducible private projection proof; their original identifiers, assigners and extension differences are preserved below.
| Stored index (zero-based) | Raw index | QuickGO ID | Assigning database | Reference | Extensions |
| --- | --- | --- | --- | --- | --- |
| 87 | 78 | UniProtKB:P21333!387295863 | BHF-UCL | PMID:10051605 | `null` |
| 87 | 79 | UniProtKB:P21333!387295864 | ComplexPortal | PMID:10051605 | `null` |
| 127 | 144 | UniProtKB:P21333!387295929 | UniProt | PMID:20458337 | `null` |
| 127 | 145 | UniProtKB:P21333!387295930 | UniProt | PMID:20458337 | `[{"connectedXrefs":[{"db":"CL","id":"0000639","relation":"part_of"}]}]` |

The two actin-organization contexts share a seed decision after source-key projection. The two exosome contexts share one exported TSV and seed row even though only one original JSON context carries its cellular extension. Neither context is discarded scientifically, and no duplicate NEW row is manufactured.
## Other original extension contexts
The exporter does not represent these structured extensions in its 16-column TSV. They remain source assertions, not edits or additional annotations. An extension question is distinguished from the validity of its main binding/location term.
| Raw index | QuickGO ID | Reference | Original structured extension |
| --- | --- | --- | --- |
| 12 | UniProtKB:P21333!387295797 | PMID:12393796 | `[{"connectedXrefs":[{"db":"GO","id":"0005737","relation":"occurs_in"}]}]` |
| 19 | UniProtKB:P21333!387295804 | PMID:16862148 | `[{"connectedXrefs":[{"db":"GO","id":"0005642","relation":"occurs_in"}]}]` |
| 47 | UniProtKB:P21333!387295832 | PMID:28297718 | `[{"connectedXrefs":[{"db":"GO","id":"0005634","relation":"occurs_in"}]}]` |
| 48 | UniProtKB:P21333!387295833 | PMID:30021884 | `[{"connectedXrefs":[{"db":"GO","id":"0005634","relation":"occurs_in"}]}]` |
| 129 | UniProtKB:P21333!387295914 | PMID:21423176 | `[{"connectedXrefs":[{"db":"CL","id":"0000057","relation":"part_of"}]}]` |
| 54 | UniProtKB:P21333!387295839 | PMID:24951510 | `[{"connectedXrefs":[{"db":"UniProtKB","id":"Q9H2S1","relation":"has_input"}]}]` |
| 85 | UniProtKB:P21333!387295870 | PMID:15684392 | `[{"connectedXrefs":[{"db":"UniProtKB","id":"P40424-1","relation":"has_input"}]}]` |
| 59 | UniProtKB:P21333!387295844 | PMID:24951510 | `[{"connectedXrefs":[{"db":"UBERON","id":"0000948","relation":"occurs_in"}]}]` |
| 143 | UniProtKB:P21333!387295928 | PMID:19056867 | `[{"connectedXrefs":[{"db":"UBERON","id":"0001088","relation":"part_of"}]}]` |
| 145 | UniProtKB:P21333!387295930 | PMID:20458337 | `[{"connectedXrefs":[{"db":"CL","id":"0000639","relation":"part_of"}]}]` |
| 146 | UniProtKB:P21333!387295931 | PMID:21362503 | `[{"connectedXrefs":[{"db":"CL","id":"0002367","relation":"part_of"}]}]` |
| 98 | UniProtKB:P21333!387295883 | PMID:24951510 | `[{"connectedXrefs":[{"db":"UniProtKB","id":"Q9H2S1","relation":"has_input"}]}]` |
| 70 | UniProtKB:P21333!387295855 | PMID:17536008 | `[{"connectedXrefs":[{"db":"UniProtKB","id":"P35462","relation":"has_input"}]}]` |
| 105 | UniProtKB:P21333!387295890 | PMID:24951510 | `[{"connectedXrefs":[{"db":"CL","id":"0002495","relation":"occurs_in"}]}]` |

## Publication access and immutable normal sources
All 64 publication records below were genuinely fetched or reused exactly from qualified main. Thirty-eight pre-existing normal sources across publications/Reactome/family scope were hydrated and hash-verified before fetch and remain unchanged. The 35 absent normal paths were acquired only within the qualified scope. The normal cache flag is reported as metadata, not a claim that all Methods, supplements or target tables were inspected. Detailed primary-reading limits accompany the annotation reasons and evidence synthesis.
| Reference | Normal cache full-text flag | Cache SHA256 |
| --- | --- | --- |
| [PMID:1833070](https://pubmed.ncbi.nlm.nih.gov/1833070/) | false | `c45bad68efcd07ae155aaad46310301cc8e038b4d0cd075973eda373d871575d` |
| [PMID:2391361](https://pubmed.ncbi.nlm.nih.gov/2391361/) | false | `ae124f18dcf36a5fb97c44585312de9e517a60a534da383c632675c525270d11` |
| [PMID:3138234](https://pubmed.ncbi.nlm.nih.gov/3138234/) | false | `f352382112d672f0dbe1ddeee8c2454461b890799f55ab44825be6b0b39d9d56` |
| [PMID:4044584](https://pubmed.ncbi.nlm.nih.gov/4044584/) | false | `505fedfb0a98c7060dd637cf63b43a83b9dee274cbe3d2ce17fb9989abb867b1` |
| [PMID:9722563](https://pubmed.ncbi.nlm.nih.gov/9722563/) | false | `c16d76abc2d8f2d2cee4175948c7eea5306c31f92ae1f45e77359d36d2a05be8` |
| [PMID:10051605](https://pubmed.ncbi.nlm.nih.gov/10051605/) | false | `e54c38e64c2746fecdbbf256f8e7d62d2bca75ff2c59d6753784813b663c4208` |
| [PMID:10604475](https://pubmed.ncbi.nlm.nih.gov/10604475/) | false | `e5f6236ed885476b3bed5cd639eb16f1a1e0fc36f58e5345f33b87730346b851` |
| [PMID:10692483](https://pubmed.ncbi.nlm.nih.gov/10692483/) | false | `6a5312209ee050c363f31dd0b51d1366a203b11987990099df2e75484f97e89a` |
| [PMID:12393796](https://pubmed.ncbi.nlm.nih.gov/12393796/) | false | `fb8bfb9dec982f3603ef41b2a1aea4f5b9de7f7288b8cff11666c16a1ceeb75b` |
| [PMID:12577067](https://pubmed.ncbi.nlm.nih.gov/12577067/) | false | `a14f9750c78006e26303c1f77bb88044d056ba71269c470d394d2d169d59dae5` |
| [PMID:12761501](https://pubmed.ncbi.nlm.nih.gov/12761501/) | false | `845d6cef9ec6e22c299a9934c487ec116386f21a8dc8b4401893a6256c7be609` |
| [PMID:14573758](https://pubmed.ncbi.nlm.nih.gov/14573758/) | false | `e0a19258c3a0243b53364ceda02fbba20a7c9f3e360c06f873f2a7f98ffed25f` |
| [PMID:15661894](https://pubmed.ncbi.nlm.nih.gov/15661894/) | false | `e4e05fc897b012d186a12fa3d8c7fdf0feaf3223e38693ea47dc701f96d67ec8` |
| [PMID:15684392](https://pubmed.ncbi.nlm.nih.gov/15684392/) | false | `e286958bf306cb3a95866de516729260c991e75684734a977407d0d29744d8b3` |
| [PMID:16076904](https://pubmed.ncbi.nlm.nih.gov/16076904/) | false | `b63ef493d8f7b666f625c5d5751fb7d9140240f76323eef6e4b5b970951ffede` |
| [PMID:16291724](https://pubmed.ncbi.nlm.nih.gov/16291724/) | false | `07136e1f7d5178ccee7fe9701e0a4cb34faf8611ef4e5cc638b1d777f995b1b6` |
| [PMID:16293600](https://pubmed.ncbi.nlm.nih.gov/16293600/) | false | `271feb41d7d437ffa5a4eaf72aecebee8173014dba2bac45d820b1e0a8e7dccc` |
| [PMID:16862148](https://pubmed.ncbi.nlm.nih.gov/16862148/) | false | `f5b6b79a036aa8c51245ca908f97256519587330a91cc4f47afc5330c94c4fc9` |
| [PMID:17408621](https://pubmed.ncbi.nlm.nih.gov/17408621/) | false | `0a3405f416979d3ce7ead0fd0b4d732b169ad5b10de3b4770cdc3f5865b2ae4f` |
| [PMID:17474147](https://pubmed.ncbi.nlm.nih.gov/17474147/) | false | `c3fdff162d5aad9393123ae3de2f041784929f80054b8b7eeb28ef6487851872` |
| [PMID:17536008](https://pubmed.ncbi.nlm.nih.gov/17536008/) | false | `7c302497772644014f4a00d7049e36b37896fd2665da0ab630bfd0f910cbbcb2` |
| [PMID:17690686](https://pubmed.ncbi.nlm.nih.gov/17690686/) | true | `c370b4a02921ab54e2fd8082f6c164f938dc12941f72298a21c4145ebc64f1fb` |
| [PMID:18177638](https://pubmed.ncbi.nlm.nih.gov/18177638/) | false | `d0a6a01640b0befcdab03156bf0c1b015944d49c3f428bd7869c096c1e53393f` |
| [PMID:18322202](https://pubmed.ncbi.nlm.nih.gov/18322202/) | false | `3f86b62d4fd442a2fa837f5267954e8fafb9f70defe4b42e162254483cd674ba` |
| [PMID:18548008](https://pubmed.ncbi.nlm.nih.gov/18548008/) | false | `5d7b05abb51287de0bd1cecef8f575337463898a4be72dcbc3aff1c191a121ee` |
| [PMID:19056867](https://pubmed.ncbi.nlm.nih.gov/19056867/) | false | `90ceb930bcd3ba708af5c0630dfcc028133affae4b73bd0409c758d54b43f2c4` |
| [PMID:19828450](https://pubmed.ncbi.nlm.nih.gov/19828450/) | false | `e5dd1d8620bcbf6dbb9b593b55022a6930996d91f751f945e1aa235f2eb6e94a` |
| [PMID:19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/) | false | `27bc1721cb6463979e40a01e57a8f855a881db7d5cce684165492ecd4d6f2337` |
| [PMID:20167606](https://pubmed.ncbi.nlm.nih.gov/20167606/) | true | `0a445597effbeb56b425ca38e0e02edec0491b0545dbb1faa13c11f0af38e8c3` |
| [PMID:20236936](https://pubmed.ncbi.nlm.nih.gov/20236936/) | true | `5b570386ec9772ec4c783a10504f53029c404bd84dbb2d61d4a7af3d05dba537` |
| [PMID:20458337](https://pubmed.ncbi.nlm.nih.gov/20458337/) | false | `82cfcf11808cf3424b9b39a17b24c4b221010856f9cc70d6e63fcc523a7591d2` |
| [PMID:20713593](https://pubmed.ncbi.nlm.nih.gov/20713593/) | true | `37d853d64bba2f64745b979b2e18ef3c0324782588b0117cb15f258b58ba91ab` |
| [PMID:21228480](https://pubmed.ncbi.nlm.nih.gov/21228480/) | false | `003400784088e4bebd5821cb448faff6f4dc480bae48e0fbfe149e7879c13367` |
| [PMID:21362503](https://pubmed.ncbi.nlm.nih.gov/21362503/) | true | `58f7dbcc96c54d80adfff4e03d452a9a6adb5525153a0746f273a6cb10cca5dd` |
| [PMID:21423176](https://pubmed.ncbi.nlm.nih.gov/21423176/) | true | `b07fc29f18f0735f07a19d469e7bdf8ba7f71a211f3b6f423f91e3dfc6170847` |
| [PMID:21524097](https://pubmed.ncbi.nlm.nih.gov/21524097/) | true | `1e8ca4622f0f735a587a378b57ab8b8e8ea73d69dfa240157936484274507de4` |
| [PMID:21653829](https://pubmed.ncbi.nlm.nih.gov/21653829/) | true | `5ba079e7f82460fdf277f904e70f430d236c66c27eee83391374c931cd7c75dd` |
| [PMID:21914078](https://pubmed.ncbi.nlm.nih.gov/21914078/) | false | `513f9e14686858c453c535b837d90fe2b078832b04befb5773fca78f318d10d7` |
| [PMID:21926999](https://pubmed.ncbi.nlm.nih.gov/21926999/) | true | `a0fc494399c6a022b3173bf24fd71d26b5e7caf5aa228ff06f4a8b7507bfff6f` |
| [PMID:22076441](https://pubmed.ncbi.nlm.nih.gov/22076441/) | false | `8ca9f075d411606e55402ab65d611e9ccd91ed641f0191d56e7dc72ea561f12b` |
| [PMID:22121117](https://pubmed.ncbi.nlm.nih.gov/22121117/) | false | `6c7ede80de1f6472ee1295d90dc40820b166709658cdcc236a4d8689e172b9a9` |
| [PMID:22307607](https://pubmed.ncbi.nlm.nih.gov/22307607/) | false | `523e018b1e0b1bf1735d024c903943228ee92720539b7bce1f576027ffce80e1` |
| [PMID:22434607](https://pubmed.ncbi.nlm.nih.gov/22434607/) | true | `a23b3a56d533e9374367fd47d1b5f8a2c5678f35caca51e56d0c574af67aa1eb` |
| [PMID:22658674](https://pubmed.ncbi.nlm.nih.gov/22658674/) | false | `0b517b543457b4dfdaeb08be8018639eae51a57a06945c05bb5e4252888cead3` |
| [PMID:22681889](https://pubmed.ncbi.nlm.nih.gov/22681889/) | false | `e3956394916d14a4ecb0b4f8fc9f3bfdcc7fc18cfa99a4c6b9538a6f31a5ebd6` |
| [PMID:22872576](https://pubmed.ncbi.nlm.nih.gov/22872576/) | false | `02eecfe11536ed222f59010220d88443336c3053667379137a6c15d989d759d1` |
| [PMID:22948144](https://pubmed.ncbi.nlm.nih.gov/22948144/) | false | `56acf09ee850326fc37c6c9ce0a39b768529b14809c86f8cc25bc71f10c6d113` |
| [PMID:23382103](https://pubmed.ncbi.nlm.nih.gov/23382103/) | true | `37869b7a9cd5ac99b5783c6be4a0ed04484076bedb8223eb81078f24c3635b1d` |
| [PMID:23525008](https://pubmed.ncbi.nlm.nih.gov/23525008/) | true | `d1e0249d2d8ab67df54c08f04f429fd0fbb292394af840b897db87600d5ba689` |
| [PMID:23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/) | true | `f347293c23617bd56d83e1ae9bc3ad8a65e540fdbf4aff13bd0e918ec598a17e` |
| [PMID:24021649](https://pubmed.ncbi.nlm.nih.gov/24021649/) | true | `a06c1e29183e39a54ac7f6401b9be78c7d91874ea3e08176a5a9acd28487c132` |
| [PMID:24951510](https://pubmed.ncbi.nlm.nih.gov/24951510/) | true | `bc0263c0fbf428518d8cd994ed9195a88a6a68397a8471f948e28c42fead6ecd` |
| [PMID:25241761](https://pubmed.ncbi.nlm.nih.gov/25241761/) | false | `e596792fcdc8dcc94dcd7750af0a78b32ad1e339cdfe116b8fcff4295727ff47` |
| [PMID:25358863](https://pubmed.ncbi.nlm.nih.gov/25358863/) | false | `da8641c7d77438eac860ffe7a384aa4890a3da0443f62910d3e2dc541e57c48d` |
| [PMID:25468996](https://pubmed.ncbi.nlm.nih.gov/25468996/) | true | `c0fe6902adfa6272ca0a1676f2125d6976d98122771aa2322ffd9bb6d4b549e0` |
| [PMID:25666618](https://pubmed.ncbi.nlm.nih.gov/25666618/) | true | `ee94bbe5740e84b025c6183cf86037b745d4d7527b61bca0c80558e9fb9eb1f5` |
| [PMID:25849143](https://pubmed.ncbi.nlm.nih.gov/25849143/) | true | `65417cb16edda696824f67269e4afd2a7821d77987296ba20c82570a5d437689` |
| [PMID:26157139](https://pubmed.ncbi.nlm.nih.gov/26157139/) | false | `fac651d5fd6623fc5cd4186a7b4634b2bcbb46c58ec8fc84a3b0d6f350bce9e4` |
| [PMID:26460884](https://pubmed.ncbi.nlm.nih.gov/26460884/) | true | `7d5194b6910c3c470fa7ccd37953ab5ec50a4347da5c5aa82bce40c43fdf782e` |
| [PMID:26496610](https://pubmed.ncbi.nlm.nih.gov/26496610/) | false | `f33c29fb4324f617e58cef04e408bb14674baffd3fe8ccb65f48fa4fa5e391a2` |
| [PMID:26972007](https://pubmed.ncbi.nlm.nih.gov/26972007/) | true | `a77370cfcb9bc0a303a2edf4c5ed47b965cc2336f3450bdc36a0a7c7a7bd46b3` |
| [PMID:28297718](https://pubmed.ncbi.nlm.nih.gov/28297718/) | true | `869778539f0669c206199940beb88de1cebf6c51aad1a83aa8e91a7819fa64e9` |
| [PMID:30021884](https://pubmed.ncbi.nlm.nih.gov/30021884/) | true | `37dcd64f8c58bf30bb7072f41859fc4658ddba2a2cc7db026c56447b874777b1` |
| [PMID:36577757](https://pubmed.ncbi.nlm.nih.gov/36577757/) | true | `9db38d0500c3d58df592069ee1660d035039127824d4559cb39d0ffdd27ed948` |

## Family provenance and ontology
Complete official PTHR38537 tree: 297 nodes; SHA256 `c4ac6ebf6fa68e9355115a5bfb860eea395f3aeb15acfa238cb796cb7365a466`. Original IBD SHA256 `0c672914e10c1f79d3fb365077d843a92e518eb6eee2aac00c67150274adf569`. The repository parser and serializer produced the one-row normal PAINT source SHA256 `81bace123a0fd1cea473868e21271eee8330bc086cd8ae7752ce0bdac04e9661`. PTN002213724 is outside the FLNA target path and no incoming FLNA IBA is present. All-family intersection was used; no bulk leaf-GAF archive was downloaded and no empty source was fabricated.
Official source: https://pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR38537 . The pinned original IBD source URL is https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf.
Cytosol/cortex-to-cytoplasm and actin-cytoskeleton-to-cytoskeleton is_a/part_of paths support the five TOO_GENERAL resolution decisions, including plasma membrane is_a membrane. The Myb-complex nuclear ancestry and intrinsic-coagulation definition support the two term-scope overannotations. Exact current term responses and relation paths were saved during the independent primary consultations; no missing ontology edge is treated as proof of biological disjointness.
## Reproduction and limitations
The private source/context proof pins the genuine seed, complete original QuickGO response, authoritative 152-row review matrix, all 73 normal sources and their main/reuse disposition. It verifies all non-review fields and row order against the seed and preserves both collapsed source groups. Validation checks are scoped to the gene, reference objects, strict GOA comparison, authored ontology terms, append-only history and a private HTML render. Status remains DRAFT because of unresolved assertions and the disclosed generic-binding advisories. No inference of universal isoform function, no new quotation and no speculative new process annotation is made.
