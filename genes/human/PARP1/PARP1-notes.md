# PARP1 (human, P09874) review notes

**Provenance note:** Provider deep research failed for this gene (Falcon returned
HTTP 402 Payment Required; Perplexity is not configured). No
`PARP1-deep-research-*.md` file exists. This notes file is a manual literature
synthesis that replaces it, built from the UniProt record (`PARP1-uniprot.txt`),
the cached publications in `publications/` (all GOA-cited PMIDs, plus four
parthanatos papers fetched with `ai-gene-review fetch-pmid`: PMID:12114629,
PMID:17116882, PMID:21467298, PMID:27846469), and the GOA annotation set.

## Identity and architecture

- Poly [ADP-ribose] polymerase 1 (ARTD1), ~113 kDa, 1014 aa. Domain order:
  Zn1 and Zn2 (PARP-type zinc fingers), NLS with the caspase-3/7 cleavage site
  (DEVD214), Zn3, BRCT-containing automodification domain, WGR domain, and the
  catalytic domain (helical subdomain HD + ART fold, catalytic Glu988).
- Gene organisation: "Each of the four metal coordinating sites putatively forming
  the two zinc fingers of the DNA-binding domain is encoded separately."
  [PMID:2513174]
- Third zinc-binding domain: "Here, we demonstrate using spectroscopic and
  crystallographic analysis that human PARP-1 has a third zinc-binding domain."
  [PMID:18055453]

## Core activity: DNA break-activated ADP-ribosyltransferase

- Catalytic: uses NAD+ to transfer ADP-ribose to acceptor residues and elongates
  chains (EC 2.4.2.30). "Stimulated by binding to nicked DNA, PARP-1 catalyzes
  poly(ADP-ribosyl)ation of the acceptor proteins and itself using NAD(+) as a
  substrate." [PMID:19764761]
- Catalytic glutamate: "Glu988 of the human polymerase aligns with the catalytic
  glutamic acid of the toxins, and replacement of this residue with Gln, Asp, or Ala
  caused major reductions in synthesis of enzyme-linked poly-ADP-ribose."
  [PMID:7852410]
- Sensor and activation: "Poly(ADP-ribose) polymerase 1 (PARP1) is a primary DNA
  damage sensor whose (ADP-ribose) polymerase activity is acutely regulated by
  interaction with DNA breaks." [PMID:22683995]; "Two flexibly linked N-terminal
  zinc fingers recognize the extreme deformability of SSBs and drive co-operative,
  stepwise self-assembly of remaining PARP-1 domains to control the activity of the
  C-terminal catalytic domain." [PMID:26626479]; activation needs local unfolding
  of the autoinhibitory HD [PMID:26626480].
- Single-molecule SSB sensing: "Quantitative smFRET and structural ensemble
  calculations reveal how PARP-1's N-terminal zinc fingers convert DNA SSBs from a
  largely unperturbed conformation, via an intermediate state into the highly kinked
  DNA conformation." [PMID:36323657]
- Residue specificity: alone, PARP1 modifies Glu/Asp; with HPF1 it modifies Ser.
  "These post-translational modifications are predominantly serine-linked and
  require the accessory factor HPF1, which is specific for the DNA damage response
  and switches the amino acid specificity of PARP1 and PARP2 from aspartate or
  glutamate to serine residues5-10." [PMID:32028527]; "Moreover, adding HPF1 to in
  vitro PARP-1/PARP-2 reactions is necessary and sufficient for serine-specific
  ADPr of histones and PARP-1 itself." [PMID:28190768]; "Serine is the major
  residue for ADP-ribosylation upon DNA damage, which strictly depends on HPF1."
  [PMID:33589610]
- Tyrosine (HPF1-dependent) [PMID:29954836, PMID:30257210]; histidine on CycT1
  [PMID:35393539]; DNA strand-break termini in vitro [PMID:27471034].
- Histone marks: H2BS6 and H3S10 ADPr convert nucleosomes into ALC1 substrates
  [PMID:34874266].
- HPF1 balance between initiation and elongation [PMID:34795260, PMID:33683197,
  PMID:34732825]; in cells serine ADPr is mainly mono-ADPr [PMID:34625544].

## DNA repair

- SSB repair / BER: "PARPs are sensors that detect single-strand break
  intermediates" and "Consequently, PARP1 deletion rescues BER and resistance to
  base damage in XRCC1-/- cells." [PMID:34102106] -- PARP1 accelerates BER but must
  be released; trapped PARP1 is toxic.
- Release/trapping: automodification releases PARP1 from DNA [PMID:26626479,
  PMID:32358582]; serine automodification at S499/S507/S519 counters trapping
  [PMID:34210965]; p97 removes trapped PARP1 [PMID:35013556].
- DSB repair and HR: Timeless co-recruitment [PMID:26344098]; nuclear cGAS
  competes with Timeless to suppress HR [PMID:30356214]; PARP9/DTX3L (BAL1/BBAP)
  recruitment [PMID:23230272]; SIRT6-dependent recruitment to DSBs [PMID:27568560].
- Replication forks: "Mechanistically, CARM1 interacts with PARP1 and promotes
  PARylation at replication forks." [PMID:33412112]

## Chromatin and transcription (context-dependent, non-core)

- "PARP-1 binds in a specific manner to nucleosomes and modulates chromatin
  structure through NAD+-dependent automodification, without modifying core
  histones or promoting the disassembly of nucleosomes." [PMID:15607977]
- Elongation: PARylation of NELF-E relieves pausing [PMID:27256882]; after DNA
  damage PARylation of CycT1 inhibits P-TEFb [PMID:35393539].
- NF-kB target genes, caspase-7 cleavage of PARP1 [PMID:22464733]; CXCL1
  coactivation [PMID:11112786].

## Innate immunity (non-core)

- Cytoplasmic PARP1 PARylates cGAS Asp191 [PMID:35460603].

## Cell death: caspase substrate and parthanatos

- Caspase-3/7 cleave PARP1 at D214; the 24 kDa N-terminal fragment binds DNA ends
  irreversibly [PMID:9721847, PMID:35104452]; the 89 kDa fragment carries PAR to the
  cytoplasm and promotes AIF-mediated apoptosis [PMID:33168626]. Here PARP1 is the
  caspase *substrate*.
- Parthanatos (PARP1-dependent, caspase-independent death): "We show that PARP-1
  activation is required for translocation of apoptosis-inducing factor (AIF) from
  the mitochondria to the nucleus and that AIF is necessary for PARP-1-dependent cell
  death." [PMID:12114629]; "Here, we identify poly(ADP-ribose) (PAR) polymer, a
  product of PARP-1 activity, as a previously uncharacterized cell death signal."
  [PMID:17116882]; "We show that AIF is a high-affinity poly(ADP-ribose)
  (PAR)-binding protein and that PAR binding to AIF is required for parthanatos both
  in vitro and in vivo." [PMID:21467298]; MIF as the downstream nuclease
  [PMID:27846469].
- Division of labour: PARP1 contributes the catalytic step (synthesis of PAR from
  NAD+). AIF release, nuclear translocation and chromatinolysis are performed by
  AIFM1 and MIF. NAD+/ATP depletion is a consequence of hyperactivation: "Upon DNA
  damage, cells undergo PARP-1-dependent ATP depletion" [PMID:24289924]; "persistent
  PARP-1 hyperactivation during severe genotoxic stress is associated with cell
  death." [PMID:26626480]
- GO representation: GO has no parthanatos term. It lists "parthanatos" as a synonym
  of GO:0070266 necroptotic process, and the GO:0097527 comment says whether it is an
  independent modality "is still being debated". That filing is mechanistically wrong:
  necroptosis is defined by RIPK1/RIPK3 and MLKL, and parthanatos needs neither. The
  ISS row to GO:0060545 positive regulation of necroptotic process is therefore
  MODIFIED to GO:0097300 programmed necrotic cell death, whose usage note covers
  regulated necrosis without shown RIPK1/RIPK3 involvement. AIFM1's GO:0060545 row is
  UNDECIDED in its own review, so it is not a convention to follow.
- Programmed or not: parthanatos is regulated (blocked by PARP1 inhibition or by
  disrupting PAR binding to AIF) but not programmed in the NCCD sense. It arises from
  PARP1 hyperactivation under severe genotoxic or excitotoxic stress, has no known
  developmental or homeostatic role, and its downstream effectors have other primary
  functions. It is kept out of core_functions; PARP1's core role is DNA repair.

## Mitochondria

- Mitochondrial PARP1 is reported, with negative effects on mtDNA repair: "In
  summary, we conclude that mitochondrial PARP1, in opposite to nuclear PARP1, exerts
  a negative effect on several mitochondrial-specific transactions including the
  repair of the mitochondrial DNA." [PMID:25378300]. Treat as non-core and contested.

## Curation decisions summary

- Core: NAD+ poly-ADP-ribosyltransferase activity (GO:0003950); HPF1-dependent
  serine ADP-ribosyltransferase (GO:0140805); single-strand-break DNA binding
  (GO:1990165) / damaged DNA binding (GO:0003684); nucleosome binding (GO:0031491);
  SSB repair, DSB repair, DNA damage response; nucleus/chromatin/site of DNA damage.
- Obsolete process terms (protein poly-ADP-ribosylation, protein
  auto-ADP-ribosylation, DNA ADP-ribosylation) were MODIFIED to the matching MF
  terms (GO:0003950, GO:0140294).
- Generic protein binding (78 rows) REMOVED as uninformative.
- Caspase-substrate-derived annotations (protein autoprocessing, apoptotic process
  from cleavage-marker papers, macrophage differentiation) fail the participation test.
