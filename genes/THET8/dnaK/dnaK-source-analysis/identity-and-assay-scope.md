# Thermus protein identity and assay scope

Official UniProt identifies Thermus thermophilus HB8 (THET8; NCBITaxon:300852) DnaK Q56235/TTHA1491 (615 residues), GrpE Q56236/TTHA1490 (177), DnaJ2 Q56237/TTHA1489 (280), and DafA P77527/TTHA1488 (78). The assayed operon J protein is current dnaJ2, not the distinct dnaJ1/TTHA0174 paralog. UniProt links the DnaK/GrpE/DnaJ2 genomic sequences to the HB8 cloning paper PMID9349721.

PDB9DVI from PMID41092901 maps by SIFTS to HB27 records Q72IK7/Q72IK5/Q72IK8, but its deposited DnaJ2 and DnaK sequences exactly match all 280 and 615 residues of the HB8 proteins. The DafA entity contains the exact 78-residue HB8 sequence after a 14-residue MKHHHHHHHHHHSG prefix. Newer results therefore transfer by exact protein sequence; the database strain mapping is not silently changed to HB8. The synthetic short DafA-tail fusion is a separate construct, not the full-length reference protein.

PMID11162122 reports no DnaJ stimulation of DnaK ATP hydrolysis under its kinetic assay conditions, while GrpE strongly accelerates nucleotide release. PMID31604242 directly measures nonnative-client binding and refolding assistance by Thermus DnaJ2; PMID41092901 resolves J-domain autoinhibition and client handoff but is not treated here as a new isolated wild-type DnaJ ATPase-stimulation assay. Thus no unconditional ATPase-activator core is assigned to THET8 DnaJ2.

DafA is an inhibitory assembly regulator, not a necessary component of the minimal productive refolding cycle. The 2025 SEC-MALS/cryo-EM result supports a 2:2:2 DnaK:DnaJ:DafA complex; historical 3:3:3 estimates relied on apparent size and are not adopted as current stoichiometry. Client-pocket occupancy and interference with J-domain docking explain inhibition without assigning ATPase chemistry to DafA.

- Official entity source: https://data.rcsb.org/rest/v1/core/polymer_entity/9DVI/1; accession comparison Q56237; saved JSON SHA256 `13173c51b7225238a1d380ab3472c708cb5cc29eecac3e3bbef065abcba1eb01`.
- Official entity source: https://data.rcsb.org/rest/v1/core/polymer_entity/9DVI/2; accession comparison Q56235; saved JSON SHA256 `7089b2ba03777b13571b95fa2df295e0e1fffd3fd6b374efa12de1dadaaf9ef8`.
- Official entity source: https://data.rcsb.org/rest/v1/core/polymer_entity/9DVI/3; accession comparison P77527; saved JSON SHA256 `e85d6dfe05b9005064b592c396c9f5e4e840151a4af4e52da3842f949763a0a2`.

Official sequence records were queried from https://rest.uniprot.org/uniprotkb/search; complete responses and primary retrieval logs remain in ignored audit cache. No acquired full article or provider report was authored into this analysis.
