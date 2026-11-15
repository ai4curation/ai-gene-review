"""Build the bounded read-only methionine-cycle preflight ledger and proofs."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def write(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source(pmid, kind, url, path, access, findings, quote=None):
    row = dict(pmid=pmid, kind=kind, url=url, source_file=path,
               access_scope=access, findings=findings)
    if path:
        row["source_sha256"] = sha(ROOT / path)
    if quote:
        row["quote"] = quote
        haystack = " ".join((ROOT / path).read_text().split())
        assert " ".join(quote.split()) in haystack, (pmid, quote)
        assert len(quote.split()) <= 25, pmid
    return row


rows = [
    source("21166890", "REVIEW", "https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2010.07455.x",
           "reviews-web-render.txt", "Publisher web-rendered cycle/SAH sections read; local XML failed and PMC challenge is not full text",
           "Distinguishes direct SAH hydrolysis from Pfs/LuxS. LuxS chemistry yields homocysteine and the DPD precursor of AI-2; signaling is not evidence that a protein performs an additional cycle reaction. Other SAM-consuming reactions yield MTA or 5'-deoxyadenosine, outside this SAH-return profile.",
           "MTA/SAH nucleosidase first converts SAH into S-ribosylhomocysteine"),
    source("18953685", "REVIEW", "https://pmc.ncbi.nlm.nih.gov/articles/mid/NIHMS78153/",
           "markham-web-followup.json", "Indexed full-text catalytic-mechanism section read; direct page returns challenge and XML retrieval failed; do not claim a complete local full-text file",
           "MetK chemistry couples methionine adenosylation to bound tripolyphosphate hydrolysis. Bacterial catalytic chemistry is distinguished from mammalian isoenzyme regulation; magnesium and monovalent-ion effects are not a universally interchangeable regulatory architecture.",
           "no covalent E·intermediates have been identified"),
    source("36891755", "REVIEW", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10491745/",
           "36891755-full.txt", "Complete XML acquired; abstract, introduction, and chemistry/boundary sections read",
           "SAM binding, SAM dependence, and a methyltransferase-like fold do not suffice for the module's SAH-producing methyl-transfer role. Radical cleavage, aminopropyl transfer, and structural SAM binding must be excluded unless the actual reaction independently produces SAH.",
           "Not all enzymes, however, utilize SAM to catalyze methylation reactions."),
    source("33534785", "PRIMARY_RESEARCH", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7857596/",
           "33534785-full.txt", "Complete XML; MesD results, comparative analysis, assay identity and methods read",
           "S. koreensis DSMZ15582 MesD Ga0059261_2929 and MesX Ga0059261_2928 jointly support heterologous methionine synthesis without folate/B12 but require oxygen. Native ADP1 ACIAD3523/3524 evidence is attributed to 18319726. The methyl donor remains unidentified. MesA/B/C/D are distinct compact synthase families, so a compact MetE-like domain alone does not specify donor chemistry.",
           "MesD requires an uncharacterized protein family (DUF1852) and oxygen for activity."),
    source("18319726", "PRIMARY_RESEARCH", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2290942/",
           "18319726-followup.txt", "Complete XML; methionine-pathway results, complementation and methods read",
           "Native A. baylyi ADP1 compact metE/ACIAD3523 is required without supplied B12; ACIAD3524 deletion causes methionine auxotrophy and gene-specific complementation restores prototrophy. These are native genetic data, not purified MesD/MesX biochemistry or an ADP1 oxygen-dependence experiment.",
           "the ACIAD3524 mutant is auxotrophic for methionine"),
    source("18840283", "PRIMARY_RESEARCH", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2606687/",
           "18840283-followup.txt", "Complete XML; model discrepancy and B12-dependent methionine-pathway results read",
           "ADP1 cannot synthesize its B12 cofactor in the tested medium; the metE deletion's lack of rescue by endogenous MetH illustrates why gene presence alone cannot satisfy a cofactor-dependent route.",
           "coenzyme-B12 is neither synthesized by A. baylyi nor provided in the experimental media"),
    source("17603473", "PRIMARY_RESEARCH", "https://www.chem.tamu.edu/rgroup/raushel/publications/P228-Nature-Activity%20Prediction-2007.pdf",
           "17603473-author.txt", "Complete author-hosted Nature PDF, main results and appended methods read",
           "Purified T. maritima TM_0936 deaminates SAH to SIH; TM_0172 hydrolyzes SIH and SAH approximately equally. This establishes matched biochemical capacity for a third SAH-return route, while the authors explicitly decline to confirm native pathway flux and cannot exclude an adenosine-deaminase physiological role. 2PLM's full 406-aa polymer exactly matches Q9X034.",
           "Tm0172 catalyses the formation of homocysteine from either SIH"),
    source("33468593", "PRIMARY_RESEARCH", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8088520/",
           "33468593-full.txt", "Complete XML; native M. smegmatis mc²155 results and strain/construct methods read",
           "Native MetE/MetH usage depends on endogenous B12 and a metE riboswitch. MetH essentiality under one context is relieved in B12-deficient genetic backgrounds. Do not call either enzyme universally essential. Correction 35289639 concerns author/acknowledgment information, not the biochemical result.",
           "transcription and translation of metE are strongly attenuated by endogenous cobalamin"),
    source("32034217", "PRIMARY_RESEARCH", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7005905/",
           "32034217-candidate.txt", "Complete XML; results, donor controls, physiological caveat and construct identity read",
           "D. mccartyi CBDB1 cbdbA481/CAI82680, current A0A916P3S8, is a 343-aa MesB/core-MetE. Purified enzyme makes methionine from methylcobalamin and homocysteine, with negative folate-donor controls. Native corrinoid-protein donation from AcsCD is a hypothesis, not a measured interface. Do not equate this enzyme with aerobic MesD or canonical full-length MetE.",
           "the physiological methyl donor might not be soluble methyl(III)cobalamin."),
    source("11489131", "PRIMARY_RESEARCH", "https://pubmed.ncbi.nlm.nih.gov/11489131/",
           "11489131-main-cache.md", "Immutable main publication-cache abstract only",
           "The abstract establishes SRH cleavage and shared biochemical intermediates in named bacteria, including E. coli. It does not expose all exact constructs or justify every quorum-sensing phenotype as a catalytic annotation.",
           "The substrate for LuxS is S-ribosylhomocysteine"),
    source("15916610", "PRIMARY_RESEARCH", "https://pubmed.ncbi.nlm.nih.gov/15916610/",
           "15916610-main-cache.md", "Immutable main publication-cache abstract only",
           "E. coli receptor-vesicle methylation supports CheR as a concrete SAM-consuming methyltransferase exemplar. Its complete main review and curated UniProt reaction already supply the SAM-to-SAH chemical connection. Reuse the main review byte-identically while #6100 owns follow-up; do not import its pending science silently.",
           "rates of assisted methylation and demethylation"),
    source("42570567", "PRIMARY_RESEARCH", "https://pubmed.ncbi.nlm.nih.gov/42570567/",
           "discovery-newmesd.json", "Abstract/metadata only; electronic publication 2026-08-07, December issue is not a future-unpublished study",
           "X. campestris pv. campestris XC1 uses MesD, S-methylmethionine-dependent MmuM, and split MetHaHb under different contexts. This identifies another real remethylation boundary. Exact XC1 sequence mapping and full text are not established here; do not substitute ATCC33913 IDs or invent a complete panel.")
]
write("reference-ledger.json", rows)

panels = [
    {"panel": "ECOLI_K12_canonical_candidate", "scope": "Complete cycle candidate after review of newly seeded MetK and one canonical remethylase; source-specific experimental strain bridges still required",
     "members": {"metK": "P0A817", "cheR": "P07364", "pfs": "P0AF12", "luxS": "P45578", "metE": "P25665", "metH_alternative": "P13009"},
     "boundary": "CheR is one concrete SAH-producing member of a distributed role, not a universal methyltransferase family. Main CheR review is COMPLETE but #6100 revisions remain separately owned."},
    {"panel": "ACIAD_ADP1_MesD_MesX", "scope": "Matched native genetic remethylation pair; partial whole-cycle panel",
     "members": {"ACIAD3523_mesD": "Q6F6Z8", "ACIAD3524_mesX": "Q6F6Z7"},
     "boundary": "Native auxotrophy/complementation in 18319726; compact-synthase reinterpretation in 33534785. Do not transfer direct S. koreensis oxygen tests or claim a known methyl donor."},
    {"panel": "THEMA_MSB8_deamination_hydrolysis", "scope": "Matched experimentally characterized two-enzyme biochemical capacity; native flux unconfirmed",
     "members": {"mtaD_TM_0936": "Q9X034", "ahcY_TM_0172": "O51933"},
     "boundary": "Same T. maritima strain annotation and paper; no archaeal MJ1388 substitution. TM_0172 also provides direct SAH hydrolysis. Exact TM0936 2PLM/Q9X034 sequence identity independently verified."},
    {"panel": "MYCS2_mc2_155_remethylation", "scope": "Native cofactor-dependent alternative-usage pair; partial whole-cycle panel",
     "members": {"metE_MSMEG_6638": "A0R6Q9", "metH_MSMEG_4185": "A0QZX6"},
     "boundary": "B12/riboswitch context determines route availability. Not M. tuberculosis and no universal essentiality claim."},
    {"panel": "DEHMC_CBDB1_MesB", "scope": "Direct catalytic remethylation exemplar, native donor interface unresolved",
     "members": {"cbdbA481_mesB": "A0A916P3S8"},
     "boundary": "343-aa enzyme tested with methylcobalamin; folate-negative result is target-specific. AcsCD donor is proposed, not established; not a complete native cycle panel."},
    {"panel": "PSEPK_KT2440_existing", "scope": "Existing gene set needs compact-synthase reassessment before whole-cycle closure",
     "members": {"metK": "Q88D60", "ahcY": "A0A140FWS3", "metH": "Q88KB5", "PP_2698_compact_mesD_candidate": "Q88JF1", "PP_2699_mesX_candidate": "Q88JF0"},
     "boundary": "344-aa PP_2698 plus adjacent DUF1852 is a source-qualified MesD/MesX inference. No native target activity or pairwise sequence analysis was performed in this preflight; a submitter metE name cannot establish the folate-specific reaction."}
]
write("candidate-panels.json", panels)
write("identity-caveats.json", {
    "Sphingomonas": "DSMZ15582 Ga0059261_2929/2928 are the actual 2021 cloned loci. Exact current UniProt mapping was not established: exact-locus query returned none; broad species results belong to other locus schemes and were not substituted.",
    "rejected_accession": {"P9WGU1": "PstS1, not SahH. Correct M. tuberculosis SahH candidate is P9WGV3; this extra candidate is not required for the minimal panel."},
    "archaeal_comparator": "PMID25917907 MJ1388 is M. jannaschii, not a bacterial SIH-hydrolase exemplar.",
    "no_custom_phylogeny": "No invented family/subfamily/PTN assignments or sequence-tree placements. Domain/neighborhood evidence is separated from experimentally established target activity.",
    "MmuM": "XC1 exact identity/full-text gap remains; bacterial S-methylmethionine-dependent remethylation must not be called impossible or omitted as an exhaustive negative.",
})

proof = {"quoted_sources": sum("quote" in r for r in rows), "all_quotes_found": True,
         "review_sources_manually_assessed": ["21166890", "18953685", "36891755"],
         "review_access_limit": "18953685 indexed catalytic section was read, not a complete local full-text acquisition",
         "tm0936_exact_sequence": json.loads((ROOT / "identity/tm-identity-proof.json").read_text()),
         "original_module_sha256": sha(ROOT / "module-original.yaml"),
         "open_pr_check": json.loads((ROOT / "duplicate-check.json").read_text())}
write("proof.json", proof)
print(json.dumps({"references": len(rows), "panels": len(panels), "quote_checks": proof["quoted_sources"]}))
