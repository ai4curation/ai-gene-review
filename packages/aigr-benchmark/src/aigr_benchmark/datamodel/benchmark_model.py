from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'bench',
     'default_range': 'string',
     'description': 'Benchmarks of protein function annotations, built CAFA-style '
                    'by time split: target annotations are those present in a '
                    'later GO release and absent from a baseline release on or '
                    'before a cutoff date. A BenchmarkSpec states the request '
                    '(species, window, aspects, evidence, size, feature quotas); a '
                    'Benchmark holds the drawn items with their target '
                    'annotations, provenance and the pinned sources they were '
                    'drawn from; a CheckReport records the deterministic checks '
                    'run over a Benchmark; an AgentEvaluation records an optional '
                    "agent's reading of it. Predictors are evaluated through a "
                    'generic interface: export writes a ClaimSet (and FASTA), any '
                    'predictor (an LLM tool, a sequence tool, an annotation '
                    'pipeline, an agent review, a curator) answers with Prediction '
                    'records, and a ScoreReport tallies them per condition and '
                    'predictor. Classes are reusable so a single item or target '
                    'annotation can be validated on its own. See '
                    'docs/benchmarks.md.',
     'id': 'https://w3id.org/ai4curation/ai-gene-review/benchmark',
     'imports': ['linkml:types'],
     'license': 'CC0',
     'name': 'benchmark',
     'prefixes': {'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'UniProtKB': {'prefix_prefix': 'UniProtKB',
                                'prefix_reference': 'http://purl.uniprot.org/uniprot/'},
                  'bench': {'prefix_prefix': 'bench',
                            'prefix_reference': 'https://w3id.org/ai4curation/ai-gene-review/benchmark/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'aigr_benchmark/schema/benchmark.yaml',
     'title': 'Time-split protein annotation benchmarks'} )

class AspectEnum(str, Enum):
    F = "F"
    """
    molecular_function
    """
    P = "P"
    """
    biological_process
    """
    C = "C"
    """
    cellular_component
    """


class BuildModeEnum(str, Enum):
    GOA_TIME_SPLIT = "GOA_TIME_SPLIT"
    """
    Targets drawn from new rows in the current GO release.
    """
    REVIEW_DERIVED = "REVIEW_DERIVED"
    """
    Targets drawn from ACCEPT and NEW annotations of ai-gene-review reviews, kept only if absent from the baseline release.
    """


class ConditionContextEnum(str, Enum):
    BLIND = "BLIND"
    """
    Sequence only; the header is withheld (the fs2f protocol).
    """
    ORGANISM = "ORGANISM"
    """
    Sequence plus organism and taxon.
    """
    FULL = "FULL"
    """
    Sequence plus the full header, accession and name included.
    """
    AGENT_REVIEW = "AGENT_REVIEW"
    """
    Combined reasoning: an agent reads the sequence and reasons over knowledge and context, as in an ai-gene-review review seeded with baseline-release annotations only.
    """


class SequenceControlEnum(str, Enum):
    NATIVE = "NATIVE"
    """
    The item's own sequence.
    """
    SHUFFLED = "SHUFFLED"
    """
    A shuffled copy of the item's sequence (the shuffle control).
    """


class VerdictEnum(str, Enum):
    yes = "yes"
    """
    The predictor affirms the claim.
    """
    no = "no"
    """
    The predictor rejects the claim.
    """
    uncertain = "uncertain"
    """
    The predictor explicitly abstains from deciding the claim.
    """


class QueryRoleEnum(str, Enum):
    TARGET = "TARGET"
    """
    A positive target; yes is correct.
    """
    NEGATED_TARGET = "NEGATED_TARGET"
    """
    A NOT target; no is correct.
    """
    DECOY = "DECOY"
    """
    A decoy term; no is expected.
    """
    SHUFFLED_TARGET = "SHUFFLED_TARGET"
    """
    A positive target asked of a shuffled sequence; no is expected.
    """


class SplitEnum(str, Enum):
    DEV = "DEV"
    TEST = "TEST"


class ItemFeatureEnum(str, Enum):
    PSEUDOENZYME = "PSEUDOENZYME"
    """
    Catalytically inactive member of an enzyme family (pseudokinase, pseudophosphatase, ...).
    """


class TargetSourceEnum(str, Enum):
    GOA_RELEASE = "GOA_RELEASE"
    AIGR_REVIEW = "AIGR_REVIEW"


class KnowledgeCategoryEnum(str, Enum):
    """
    CAFA knowledge categories, judged at the baseline release on experimental evidence.
    """
    NO_KNOWLEDGE = "NO_KNOWLEDGE"
    """
    No experimental annotation in any aspect.
    """
    LIMITED_KNOWLEDGE = "LIMITED_KNOWLEDGE"
    """
    Experimental annotation in another aspect, none in this one.
    """
    PARTIAL_KNOWLEDGE = "PARTIAL_KNOWLEDGE"
    """
    Experimental annotation already in this aspect; the target adds to it.
    """


class DifficultyEnum(str, Enum):
    EASY = "EASY"
    """
    The term or a descendant was already predicted on the protein (IBA, IEA, ISS, ...) or experimentally annotated on a close homolog before the cutoff.
    """
    MEDIUM = "MEDIUM"
    """
    A baseline experimental term on the protein is a near-duplicate (Lin similarity at or above the threshold).
    """
    HARD = "HARD"
    """
    None of the above.
    """


class CheckEnum(str, Enum):
    schema = "schema"
    novelty = "novelty"
    """
    Target (or a descendant, or an obsolete term mapped to it) absent from the baseline release with experimental evidence.
    """
    present_in_current = "present_in_current"
    """
    The target row is in the current release.
    """
    date_window = "date_window"
    """
    GAF date on or after the cutoff (informational; GO re-stamps dates).
    """
    near_duplicate = "near_duplicate"
    homolog_leakage = "homolog_leakage"
    prior_prediction = "prior_prediction"
    """
    Term or a descendant predicted on the protein before the cutoff (IBA/PAN-GO, IEA, ISS, ...).
    """
    uniprot_leakage = "uniprot_leakage"
    """
    Current UniProt entry exposes the target (DR GO line or label in comments).
    """
    review_agreement = "review_agreement"
    """
    Agreement with an ai-gene-review review of the gene, where one exists.
    """
    reference_recency = "reference_recency"
    """
    Target reference published after each condition's model training cutoff.
    """
    header_leakage = "header_leakage"
    """
    The protein name shown in FULL-header conditions does not give the target label away.
    """
    feature_label = "feature_label"
    """
    A query-derived feature label is supported by the UniProt protein name, not only by comment text.
    """
    decoy = "decoy"
    """
    Decoy terms are unrelated (neither way) to the protein's current annotations.
    """
    balance = "balance"
    difficulty = "difficulty"
    """
    A recorded difficulty disagrees with the grading checks.
    """


class CheckStatusEnum(str, Enum):
    PASS = "PASS"
    INFO = "INFO"
    WARN = "WARN"
    FAIL = "FAIL"


class AgentFindingCategoryEnum(str, Enum):
    OK = "OK"
    AMBIGUOUS_TARGET = "AMBIGUOUS_TARGET"
    WRONG_TARGET = "WRONG_TARGET"
    TRIVIAL_TARGET = "TRIVIAL_TARGET"
    LEAKAGE = "LEAKAGE"
    IMBALANCE = "IMBALANCE"
    OTHER = "OTHER"



class BenchmarkSpec(ConfiguredBaseModel):
    """
    The request a benchmark is built from. Everything the builder needs is here, so the spec plus its pinned sources reproduce the benchmark.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    id: str = Field(default=..., description="""Short benchmark identifier, used for the folder and file names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'Taxon',
                       'Benchmark',
                       'BenchmarkItem',
                       'Term',
                       'Claim']} })
    title: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'Benchmark']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'EvaluationCondition',
                       'Predictor',
                       'Benchmark']} })
    taxon: Taxon = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'BenchmarkItem']} })
    cutoff_date: date = Field(default=..., description="""Knowledge cutoff. The baseline release must be on or before this date; annotations absent from it are candidates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    baseline_release: str = Field(default=..., description="""GO release date (YYYY-MM-DD) used as the pre-cutoff snapshot. Must be on or before cutoff_date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    current_release: str = Field(default=..., description="""GO release date (YYYY-MM-DD) the target annotations are drawn from. Must be after cutoff_date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    aspects: Optional[list[AspectEnum]] = Field(default=None, description="""Aspects to draw targets from; all three if omitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    go_branches: Optional[list[str]] = Field(default=None, description="""Optional GO ids; when given, a target term must be the id or a descendant (is_a/part_of) of one of them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    evidence_codes: Optional[list[str]] = Field(default=None, description="""Evidence codes that qualify a target. Defaults to the CAFA experimental set EXP IDA IPI IMP IGI IEP TAS IC.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    excluded_terms: Optional[list[str]] = Field(default=None, description="""Terms never used as targets. Defaults to the aspect roots, binding and protein binding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    include_negated: Optional[bool] = Field(default=None, description="""Also take NOT annotations as (negative) targets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    max_proteins_per_reference: Optional[int] = Field(default=None, description="""A reference that adds new annotations to more proteins than this is treated as high-throughput and its rows are not used as targets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    size: int = Field(default=..., description="""Number of items (proteins) to draw, including feature quotas.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    dev_fraction: Optional[float] = Field(default=None, description="""Fraction of items assigned to the DEV split (seeded); the rest are TEST.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    seed: Optional[int] = Field(default=None, description="""Random seed for sampling and split assignment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    features: Optional[list[FeatureQuota]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'BenchmarkItem']} })
    mode: Optional[BuildModeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    near_duplicate_threshold: Optional[float] = Field(default=None, description="""Lin similarity at or above which a target counts as a near-duplicate of a baseline term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    min_reference_date: Optional[date] = Field(default=None, description="""Optional. Keep only targets whose PubMed reference was published on or after this date (targets with non-PMID references are dropped).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'FeatureQuota']} })
    decoys_per_item: Optional[int] = Field(default=None, description="""Decoy terms per item: terms drawn from other items' targets that are not entailed by, and do not entail, any current annotation of the protein. They measure a predictor's tendency to say yes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    conditions: Optional[list[EvaluationCondition]] = Field(default=None, description="""The evaluation conditions a run compares per item, for example a sequence-only blind read against an agent reasoning over sequence, knowledge and context. A condition says what a predictor may see, not which predictor is run.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })
    predictors: Optional[list[Predictor]] = Field(default=None, description="""Predictors planned for or run on this benchmark. Optional; listed so the reference_recency check can compare target dates with each predictor's training cutoff before any run.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec']} })

    @field_validator('baseline_release')
    def pattern_baseline_release(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid baseline_release format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid baseline_release format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('current_release')
    def pattern_current_release(cls, v):
        pattern=re.compile(r"^\d{4}-\d{2}-\d{2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid current_release format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid current_release format: {v}"
            raise ValueError(err_msg)
        return v


class EvaluationCondition(ConfiguredBaseModel):
    """
    What a predictor is allowed to see about each item. Conditions differ in what the predictor is shown, so comparing them per item separates reading the sequence from recalling or retrieving knowledge about the named protein. Any predictor can be run under any condition it supports.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationCondition', 'Predictor', 'SourceSnapshot']} })
    context: ConditionContextEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationCondition', 'Prediction']} })
    shuffle_control: Optional[bool] = Field(default=None, description="""Also ask of a shuffled copy of each sequence (predictions marked sequence_control SHUFFLED), to measure yes answers that do not depend on the sequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationCondition']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'EvaluationCondition',
                       'Predictor',
                       'Benchmark']} })


class Predictor(ConfiguredBaseModel):
    """
    A configured predictor: a tool, model or person, with the settings that change its answers. Two runs of one tool with different models are different predictors.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    name: str = Field(default=..., description="""Predictor name as Prediction records give it, for example peptalk:claude-opus-5-5, interproscan, ai-gene-review:claude-opus-5-5 or a curator's ORCID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationCondition', 'Predictor', 'SourceSnapshot']} })
    version: Optional[str] = Field(default=None, description="""Tool or pipeline version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Predictor']} })
    model: Optional[str] = Field(default=None, description="""Underlying model, when the predictor is a model or uses one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Predictor', 'Prediction']} })
    effort: Optional[str] = Field(default=None, description="""Reasoning effort or thinking level, in the provider's own labels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Predictor', 'Prediction']} })
    model_training_cutoff: Optional[date] = Field(default=None, description="""Training data cutoff of the model. Targets whose reference predates it may be known to the model from the literature, whatever the GO release dates say.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Predictor']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'EvaluationCondition',
                       'Predictor',
                       'Benchmark']} })


class FeatureQuota(ConfiguredBaseModel):
    """
    Request that some items carry a feature, such as being a pseudoenzyme. Candidates come from a UniProt query; the label is UniProt's, not a literature check, and is recorded as such.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    feature: ItemFeatureEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['FeatureQuota', 'ItemFeature']} })
    uniprot_query: str = Field(default=..., description="""UniProtKB query whose hits are the feature's candidate proteins.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FeatureQuota']} })
    count: int = Field(default=..., description="""Maximum number of items with this feature.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FeatureQuota', 'CountTable']} })
    min_reference_date: Optional[date] = Field(default=None, description="""Overrides the spec's min_reference_date for this quota, for features too rare to fill from the main window.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'FeatureQuota']} })


class Taxon(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'Taxon',
                       'Benchmark',
                       'BenchmarkItem',
                       'Term',
                       'Claim']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon', 'Term']} })
    gaf_code: Optional[str] = Field(default=None, description="""Species code used in GO release file names (HUMAN for annotations/gaf/HUMAN-uniprot.gaf.gz; goa_human in older releases).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^NCBITaxon:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class Benchmark(ConfiguredBaseModel):
    """
    A drawn benchmark.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark',
         'tree_root': True})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'Taxon',
                       'Benchmark',
                       'BenchmarkItem',
                       'Term',
                       'Claim']} })
    title: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'Benchmark']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'EvaluationCondition',
                       'Predictor',
                       'Benchmark']} })
    created: date = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Benchmark']} })
    spec: BenchmarkSpec = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Benchmark']} })
    sources: Optional[list[SourceSnapshot]] = Field(default=None, description="""Every external input, pinned by release and checksum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Benchmark', 'CheckReport']} })
    items: list[BenchmarkItem] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Benchmark']} })


class SourceSnapshot(ConfiguredBaseModel):
    """
    One pinned input file or query.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    name: str = Field(default=..., description="""Role of the source, for example baseline_gaf or current_ontology.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationCondition', 'Predictor', 'SourceSnapshot']} })
    url: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SourceSnapshot']} })
    release: Optional[str] = Field(default=None, description="""Release identifier (GO release date, UniProt release).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceSnapshot']} })
    sha256: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SourceSnapshot']} })
    retrieved: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SourceSnapshot']} })
    query: Optional[str] = Field(default=None, description="""For a query source, the query string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceSnapshot']} })


class BenchmarkItem(ConfiguredBaseModel):
    """
    One protein with its target annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'Taxon',
                       'Benchmark',
                       'BenchmarkItem',
                       'Term',
                       'Claim']} })
    protein: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem', 'Claim']} })
    gene_symbol: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    protein_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    entry_name: Optional[str] = Field(default=None, description="""UniProtKB entry name (mnemonic), used in the FASTA header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    taxon: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'BenchmarkItem']} })
    sequence: Optional[str] = Field(default=None, description="""Canonical UniProtKB sequence at sequence_version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    sequence_version: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    split: SplitEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    features: Optional[list[ItemFeature]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec', 'BenchmarkItem']} })
    target_annotations: list[TargetAnnotation] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    decoys: Optional[list[DecoyTerm]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem']} })
    difficulty: Optional[DifficultyEnum] = Field(default=None, description="""The hardest difficulty among the item's targets.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem', 'TargetAnnotation']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem', 'ItemFeature', 'TargetAnnotation']} })

    @field_validator('protein')
    def pattern_protein(cls, v):
        pattern=re.compile(r"^UniProtKB:[A-Z0-9]+(-\d+)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('taxon')
    def pattern_taxon(cls, v):
        pattern=re.compile(r"^NCBITaxon:\d+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid taxon format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid taxon format: {v}"
            raise ValueError(err_msg)
        return v


class ItemFeature(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    feature: ItemFeatureEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['FeatureQuota', 'ItemFeature']} })
    source: str = Field(default=..., description="""Where the label came from, for example the UniProt query that matched.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ItemFeature', 'TargetAnnotation']} })
    literature_checked: Optional[bool] = Field(default=None, description="""True only when someone read the literature behind the label. A UniProt name containing \"inactive\" is not a literature check.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ItemFeature']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem', 'ItemFeature', 'TargetAnnotation']} })


class TargetAnnotation(ConfiguredBaseModel):
    """
    An annotation a predictor should recover (or, if negated, should not assert).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    term: Term = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation', 'DecoyTerm', 'Claim', 'Prediction']} })
    aspect: AspectEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation', 'DecoyTerm']} })
    qualifier: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    negated: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    evidence_code: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    reference: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    with_from: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    assigned_by: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    gaf_date: Optional[str] = Field(default=None, description="""The GAF date column (YYYYMMDD). GO re-stamps it, so it is not proof of newness.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    reference_date: Optional[date] = Field(default=None, description="""PubMed publication date (sortpubdate) of the reference. The builder picks the earliest-published supporting reference as the target's reference, since that is when the knowledge became readable. The record date can be later than a preprint of the same work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    supporting_references: Optional[list[str]] = Field(default=None, description="""Every reference in the current release supporting this term on this protein (including reference), when there is more than one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    source: TargetSourceEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ItemFeature', 'TargetAnnotation']} })
    review_action: Optional[str] = Field(default=None, description="""Action an ai-gene-review review gave this annotation, when one exists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    review_file: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    knowledge_category: Optional[KnowledgeCategoryEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation']} })
    difficulty: Optional[DifficultyEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem', 'TargetAnnotation']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem', 'ItemFeature', 'TargetAnnotation']} })


class DecoyTerm(ConfiguredBaseModel):
    """
    A term the protein is not annotated to, used as a negative control. Absence of an annotation is not a measurement that the protein lacks the function, so a yes on a decoy is not necessarily wrong.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    term: Term = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation', 'DecoyTerm', 'Claim', 'Prediction']} })
    aspect: AspectEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation', 'DecoyTerm']} })
    drawn_from: Optional[str] = Field(default=None, description="""Item whose target supplied the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DecoyTerm']} })


class Term(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'Taxon',
                       'Benchmark',
                       'BenchmarkItem',
                       'Term',
                       'Claim']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Taxon', 'Term']} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^GO:\d{7}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class CheckReport(ConfiguredBaseModel):
    """
    Results of the deterministic checks over one benchmark.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    benchmark_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport',
                       'ClaimSet',
                       'PredictionSet',
                       'ScoreReport',
                       'AgentEvaluation']} })
    generated: date = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport', 'ScoreReport']} })
    sources: Optional[list[SourceSnapshot]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Benchmark', 'CheckReport']} })
    summary: Optional[list[CheckSummary]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport']} })
    results: Optional[list[CheckResult]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport']} })
    stats: Optional[BenchmarkStats] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport']} })


class CheckSummary(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    check: CheckEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckSummary', 'CheckResult']} })
    passed: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckSummary']} })
    info: Optional[int] = Field(default=None, description="""INFO results, including checks that could not be performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CheckSummary']} })
    warned: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckSummary']} })
    failed: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckSummary']} })


class CheckResult(ConfiguredBaseModel):
    """
    One check on one target annotation, item, or the whole benchmark.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    check: CheckEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckSummary', 'CheckResult']} })
    status: CheckStatusEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult']} })
    item_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult',
                       'Claim',
                       'Prediction',
                       'ConditionScore',
                       'AgentFinding']} })
    term_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult', 'AgentFinding']} })
    message: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult']} })
    evidence: Optional[list[str]] = Field(default=None, description="""Rows or values the result rests on, for example a baseline GAF row.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult', 'Prediction']} })


class BenchmarkStats(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    n_items: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })
    n_targets: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })
    counts: Optional[list[CountTable]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })
    targets_per_item_min: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })
    targets_per_item_median: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })
    targets_per_item_max: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })
    mean_information_content: Optional[float] = Field(default=None, description="""Mean IC (bits, from baseline annotation frequencies) of target terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })
    top_reference_share: Optional[float] = Field(default=None, description="""Fraction of targets that come from the most frequent reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkStats']} })


class CountTable(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    dimension: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CountTable']} })
    value: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CountTable']} })
    count: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['FeatureQuota', 'CountTable']} })


class Claim(ConfiguredBaseModel):
    """
    One question a predictor is asked: does the protein of this item have this GO term? A claim never says whether its term is a target, a NOT target or a decoy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    id: str = Field(default=..., description="""<item id>/<GO term id>.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkSpec',
                       'Taxon',
                       'Benchmark',
                       'BenchmarkItem',
                       'Term',
                       'Claim']} })
    item_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult',
                       'Claim',
                       'Prediction',
                       'ConditionScore',
                       'AgentFinding']} })
    protein: str = Field(default=..., description="""UniProtKB CURIE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkItem', 'Claim']} })
    sequence_id: str = Field(default=..., description="""Id of the item's record in the exported FASTA.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Claim']} })
    term: Term = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation', 'DecoyTerm', 'Claim', 'Prediction']} })


class ClaimSet(ConfiguredBaseModel):
    """
    The claims exported for a benchmark, written as <id>-claims.yaml.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    benchmark_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport',
                       'ClaimSet',
                       'PredictionSet',
                       'ScoreReport',
                       'AgentEvaluation']} })
    claims: Optional[list[Claim]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ClaimSet']} })


class Prediction(ConfiguredBaseModel):
    """
    One predictor's answer to one claim under one condition. This is the only format `benchmark score` reads; importers convert each predictor's native output into it. A prediction names its claim by claim_id or by item_id plus term. If a recorded attempt returned no answer, omit both verdict and score to count the attempt as missing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark',
         'rules': [{'postconditions': {'any_of': [{'slot_conditions': {'claim_id': {'name': 'claim_id',
                                                                                    'pattern': '.+/.+',
                                                                                    'required': True}}},
                                                  {'slot_conditions': {'term': {'name': 'term',
                                                                                'pattern': '.+',
                                                                                'required': True}}}]},
                    'preconditions': {'slot_conditions': {'item_id': {'name': 'item_id',
                                                                      'required': True}}}}]})

    item_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult',
                       'Claim',
                       'Prediction',
                       'ConditionScore',
                       'AgentFinding']} })
    claim_id: Optional[str] = Field(default=None, description="""Id of the Claim answered; optional when term is given.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    term: Optional[str] = Field(default=None, description="""GO term id the prediction is about; optional when claim_id is given.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TargetAnnotation', 'DecoyTerm', 'Claim', 'Prediction']} })
    predictor: str = Field(default=..., description="""Predictor name; see Predictor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction', 'ConditionScore']} })
    predictor_version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    model: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Predictor', 'Prediction']} })
    effort: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Predictor', 'Prediction']} })
    condition: str = Field(default=..., description="""Name of an EvaluationCondition in the spec.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction', 'ConditionScore']} })
    context: Optional[ConditionContextEnum] = Field(default=None, description="""The condition's context level, for records read without the spec.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvaluationCondition', 'Prediction']} })
    sequence_control: Optional[SequenceControlEnum] = Field(default=None, description="""Whether the native or a shuffled sequence was shown (default NATIVE).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    verdict: Optional[VerdictEnum] = Field(default=None, description="""The predictor's answer; absent when it gave none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    score: Optional[float] = Field(default=None, description="""A numeric score for the claim, for predictors that give one (a probability, an E-value-derived score). Scored as a verdict only with an explicit threshold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    confidence: Optional[float] = Field(default=None, description="""The predictor's stated confidence in its verdict, 0 to 1.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    evidence: Optional[str] = Field(default=None, description="""The predictor's stated reasoning or evidence, verbatim or abridged.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult', 'Prediction']} })
    cost_usd: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    prediction_date: Optional[date] = Field(default=None, description="""When the prediction was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })
    provenance: Optional[str] = Field(default=None, description="""Where the record came from, for example the native output file and record id.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction']} })


class PredictionSet(ConfiguredBaseModel):
    """
    A YAML file of predictions. JSONL files hold one Prediction per line instead, and are validated as a PredictionSet without a benchmark_id.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    benchmark_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport',
                       'ClaimSet',
                       'PredictionSet',
                       'ScoreReport',
                       'AgentEvaluation']} })
    predictions: Optional[list[Prediction]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['PredictionSet']} })


class ScoreReport(ConfiguredBaseModel):
    """
    Verdicts of each predictor under each condition on each item's targets, NOT targets and decoys, tallied overall and per item so conditions and predictors can be compared item by item.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    benchmark_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport',
                       'ClaimSet',
                       'PredictionSet',
                       'ScoreReport',
                       'AgentEvaluation']} })
    generated: date = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport', 'ScoreReport']} })
    inputs: Optional[list[str]] = Field(default=None, description="""Prediction files scored, each with its sha256.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScoreReport']} })
    condition_scores: Optional[list[ConditionScore]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ScoreReport']} })
    item_scores: Optional[list[ConditionScore]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ScoreReport']} })


class ConditionScore(ConfiguredBaseModel):
    """
    Verdict counts for one condition and predictor (and, in item_scores, one item) and one query role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    condition: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction', 'ConditionScore']} })
    predictor: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Prediction', 'ConditionScore']} })
    item_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult',
                       'Claim',
                       'Prediction',
                       'ConditionScore',
                       'AgentFinding']} })
    role: QueryRoleEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionScore']} })
    n: int = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionScore']} })
    n_yes: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionScore']} })
    n_no: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionScore']} })
    n_uncertain: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionScore']} })
    n_missing: Optional[int] = Field(default=None, description="""Queries with no verdict (not asked, failed, or null).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConditionScore']} })


class AgentEvaluation(ConfiguredBaseModel):
    """
    An agent's reading of a finished benchmark. These are judgements, not expert review; each finding should name a deterministic check that would confirm it, so objections are tested against the data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    benchmark_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CheckReport',
                       'ClaimSet',
                       'PredictionSet',
                       'ScoreReport',
                       'AgentEvaluation']} })
    evaluator: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AgentEvaluation']} })
    evaluation_date: date = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AgentEvaluation']} })
    overall_assessment: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AgentEvaluation']} })
    findings: Optional[list[AgentFinding]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['AgentEvaluation']} })


class AgentFinding(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/ai-gene-review/benchmark'})

    item_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult',
                       'Claim',
                       'Prediction',
                       'ConditionScore',
                       'AgentFinding']} })
    term_id: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CheckResult', 'AgentFinding']} })
    category: AgentFindingCategoryEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AgentFinding']} })
    severity: CheckStatusEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AgentFinding']} })
    explanation: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['AgentFinding']} })
    proposed_check: Optional[str] = Field(default=None, description="""A deterministic test that would confirm or refute the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AgentFinding']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
BenchmarkSpec.model_rebuild()
EvaluationCondition.model_rebuild()
Predictor.model_rebuild()
FeatureQuota.model_rebuild()
Taxon.model_rebuild()
Benchmark.model_rebuild()
SourceSnapshot.model_rebuild()
BenchmarkItem.model_rebuild()
ItemFeature.model_rebuild()
TargetAnnotation.model_rebuild()
DecoyTerm.model_rebuild()
Term.model_rebuild()
CheckReport.model_rebuild()
CheckSummary.model_rebuild()
CheckResult.model_rebuild()
BenchmarkStats.model_rebuild()
CountTable.model_rebuild()
Claim.model_rebuild()
ClaimSet.model_rebuild()
Prediction.model_rebuild()
PredictionSet.model_rebuild()
ScoreReport.model_rebuild()
ConditionScore.model_rebuild()
AgentEvaluation.model_rebuild()
AgentFinding.model_rebuild()
