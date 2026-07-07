# UGP2 (UDP-glucose pyrophosphorylase 2) — curation notes

UniProt: Q16851 (UGPA_HUMAN). HGNC:12527. Gene 7360. Chr 2. 508 aa (isoform 1).

## Core biology

UGP2 is the human **UTP:glucose-1-phosphate uridylyltransferase** (UDP-glucose
pyrophosphorylase, UDPGP/UGPase), **EC 2.7.7.9**. It reversibly catalyses:

  alpha-D-glucose 1-phosphate + UTP + H+  <=>  UDP-alpha-D-glucose + diphosphate
  (Rhea:RHEA:19889; physiological direction left-to-right, Rhea:RHEA:19890)

UDP-glucose is the universal activated glucosyl donor. It is the direct precursor for:
- **glycogen synthesis** (via glycogenin/glycogen synthase, GYS)
- **protein/lipid glycosylation** (UGGT glucosyltransferases; N-glycosylation)
- **UDP-glucuronic acid** synthesis (via UGDH) → glucuronidation, GAG/proteoglycan synthesis
- galactose (Leloir) interconversion.

UGP2 is described as the ONLY known mammalian enzyme capable of converting
glucose-1-phosphate to UDP-glucose [PMID:31820119; PMID:34330832].

Structure: cytosolic **homooctamer** (UDPGP type 1 family); octamerization via
end-to-end and side-by-side interactions; a "latch loop" modulates activity
[PMID:22132858 SUBUNIT/X-ray]. Active site ~Asp396; Mg2+-dependent.

Two isoforms by alternative first exon: isoform 1 ("long", Q16851-1, 508 aa,
"Muscle-II") and isoform 2 ("short", Q16851-2, "Muscle-I", lacks residues 1-11).
Note the historical UGP1/UGP2 confusion: UGP1 (PMID:8354390) probably does not
exist and corresponds to UGP2 (UniProt CAUTION).

## Disease

Bi-allelic isoform-2 start-loss variant → **Developmental and epileptic
encephalopathy 83 (DEE83)** [MIM:618744], autosomal recessive; only the brain-relevant
short isoform is lost, sparing whole-organism lethality [PMID:31820119].

## Cancer

UGP2 is a YAP–TEAD target gene; required for pancreatic ductal adenocarcinoma
growth via glycogen synthesis and N-glycosylation (e.g. EGFR N-glycosylation)
[PMID:34330832].

## Key supporting quotes (verbatim; grep-verified)

- Catalysis / role, PMID:31820119: "UGP2 is an essential octameric enzyme in nucleotide
  sugar metabolism [38, 39, 121], as it is the only known enzyme capable of catalyzing the
  conversion of glucose-1-phosphate to UDP-glucose [36, 108]. UDP-glucose is a crucial
  precursor for the production of glycogen by glycogen synthase (GYS) [2, 44]..."
- Glycogen/glycosylation, PMID:31820119: "...reduced synthesis of UDP-glucose, leading to
  defects in glycogen synthesis and protein glycosylation and to the activation of UPR response."
- PMID:34330832 (abstract): "UDP-glucose pyrophosphorylase 2 (UGP2), the enzyme that
  synthesizes uridine diphosphate (UDP)-glucose..."
- PMID:34330832 (full text): "The use of glucose in these pathways depends on its activation
  to uridine diphosphate (UDP)-glucose catalyzed by UDP-glucose pyrophosphorylase 2 (UGP2),
  the only enzyme capable of converting glucose 1-phosphate to UDP-glucose in mammalian cells (6)."
- PMID:34330832: "An important cellular process that utilizes UDP-glucose as a direct
  precursor is glycogen synthesis (18)." / "we found that knockdown of YAP, which decreases
  UGP2 expression, led to a decrease in intracellular UDP-glucose and glycogen levels in PDAC cells"
- Kinetics, PMID:8631325: "UDP-Glc pyrophosphorylase (EC 2.7.7.9) catalyses the
  interconversion of MgUTP plus Glc1P and UDP-Glc plus MgPPi."
- Structure, PMID:22132858: "the crystal structure of hUGPase (human UGPase) was determined
  and shown to form octamers through end-to-end and side-by-side interactions."
- Reactome R-HSA-70286: "Cytosolic UDP-glucose pyrophosphorylase 2 (UGP2) catalyzes the
  reaction of UTP and glucose 1-phosphate to form UDP glucose and pyrophosphate..."
- Cloning/tissue, PMID:8354390: "A human liver cDNA clone which encodes the UDP-glucose
  pyrophosphorylase was isolated by complementation of a bacterial galU mutant."

## GOA overview (42 lines)

MF: GO:0003983 (UTP:glucose-1-phosphate uridylyltransferase) IBA/IEA/IDA/IMP/TAS — core, ACCEPT.
GO:0070569 uridylyltransferase activity (IEA, InterPro) - parent of GO:0003983, MODIFY to 0003983.
NOTE schema shapes: proposed_replacement_terms = list of Term objects (id+label); core_functions.directly_involved_in = LIST of Term; suggested_questions = list of {question:}; suggested_experiments = list of {description:}.
GO:0051748 UTP-monosaccharide-1-phosphate uridylyltransferase (IEA Ensembl) — broader parent, ACCEPT non-core.
BP: GO:0006011 UDP-alpha-D-glucose metabolic process — core, ACCEPT.
GO:0005977 glycogen metabolic process (IBA); GO:0005978 glycogen biosynthetic process (IEA/IMP) — ACCEPT.
CC: GO:0005737 cytoplasm (IBA/IEA/EXP); GO:0005829 cytosol (TAS Reactome) — ACCEPT (cytosol is more precise, core).
GO:0070062 extracellular exosome (HDA ×3) — MARK_AS_OVER_ANNOTATED (proteomic contaminant, not functional site).
GO:0005634 nucleus (HDA, sperm nucleus proteome) — MARK_AS_OVER_ANNOTATED.
GO:0005515 protein binding (IPI ×5) — MARK_AS_OVER_ANNOTATED (uninformative; keep evidence, not core).
GO:0042802 identical protein binding (IPI ×4) — ACCEPT non-core (supports homooctamer, real).
GO:0007420 brain development (IMP, PMID:31820119) — KEEP_AS_NON_CORE (disease/tissue-relevance, not molecular core).
</content>
