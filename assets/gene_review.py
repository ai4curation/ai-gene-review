# Auto generated from gene_review.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-02-02T09:21:18
# Schema: gene_review
#
# id: https://ai4curation.io/ai-gene-review
# description: Schema for gene curation Top level entity is a GeneReview, which is about a single gene (and its equivalent swiss-prot entry). It contains a high level summary of the gene, plus a review of all existing annotations. It also contains a list of core functions, which are GO-CAM-like annotons describing the core evolved functions of the gene.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Namespaces
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GENE_REVIEW = CurieNamespace('gene_review', 'https://w3id.org/ai4curation/gene_review/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OA = CurieNamespace('oa', 'http://www.w3.org/ns/oa#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GENE_REVIEW


# Types

# Class references
class GeneReviewId(extended_str):
    pass


class AlternativeProductId(extended_str):
    pass


class FunctionalIsoformId(extended_str):
    pass


class TermId(extended_str):
    pass


class ReferenceId(extended_str):
    pass


class RuleReviewId(extended_str):
    pass


class RuleReviewEntryId(extended_str):
    pass


@dataclass(repr=False)
class GeneReview(YAMLRoot):
    """
    Complete review for a gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GeneReview"]
    class_class_curie: ClassVar[str] = "gene_review:GeneReview"
    class_name: ClassVar[str] = "GeneReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GeneReview

    id: Union[str, GeneReviewId] = None
    gene_symbol: str = None
    taxon: Union[dict, "Term"] = None
    product_type: Optional[Union[str, "ProductTypeEnum"]] = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    tags: Optional[Union[str, list[str]]] = empty_list()
    status: Optional[Union[str, "GeneReviewStatusEnum"]] = None
    description: Optional[str] = None
    alternative_products: Optional[Union[dict[Union[str, AlternativeProductId], Union[dict, "AlternativeProduct"]], list[Union[dict, "AlternativeProduct"]]]] = empty_dict()
    functional_isoforms: Optional[Union[dict[Union[str, FunctionalIsoformId], Union[dict, "FunctionalIsoform"]], list[Union[dict, "FunctionalIsoform"]]]] = empty_dict()
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, "Reference"]], list[Union[dict, "Reference"]]]] = empty_dict()
    existing_annotations: Optional[Union[Union[dict, "ExistingAnnotation"], list[Union[dict, "ExistingAnnotation"]]]] = empty_list()
    core_functions: Optional[Union[Union[dict, "CoreFunction"], list[Union[dict, "CoreFunction"]]]] = empty_list()
    proposed_new_terms: Optional[Union[Union[dict, "ProposedOntologyTerm"], list[Union[dict, "ProposedOntologyTerm"]]]] = empty_list()
    suggested_questions: Optional[Union[Union[dict, "Question"], list[Union[dict, "Question"]]]] = empty_list()
    suggested_experiments: Optional[Union[Union[dict, "Experiment"], list[Union[dict, "Experiment"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneReviewId):
            self.id = GeneReviewId(self.id)

        if self._is_empty(self.gene_symbol):
            self.MissingRequiredField("gene_symbol")
        if not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self._is_empty(self.taxon):
            self.MissingRequiredField("taxon")
        if not isinstance(self.taxon, Term):
            self.taxon = Term(**as_dict(self.taxon))

        if self.product_type is not None and not isinstance(self.product_type, ProductTypeEnum):
            self.product_type = ProductTypeEnum(self.product_type)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        if self.status is not None and not isinstance(self.status, GeneReviewStatusEnum):
            self.status = GeneReviewStatusEnum(self.status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="alternative_products", slot_type=AlternativeProduct, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="functional_isoforms", slot_type=FunctionalIsoform, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="existing_annotations", slot_type=ExistingAnnotation, key_name="evidence_type", keyed=False)

        self._normalize_inlined_as_dict(slot_name="core_functions", slot_type=CoreFunction, key_name="molecular_function", keyed=False)

        self._normalize_inlined_as_dict(slot_name="proposed_new_terms", slot_type=ProposedOntologyTerm, key_name="proposed_name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="suggested_questions", slot_type=Question, key_name="question", keyed=False)

        self._normalize_inlined_as_dict(slot_name="suggested_experiments", slot_type=Experiment, key_name="description", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlternativeProduct(YAMLRoot):
    """
    An alternative splicing product (isoform) of the gene. Corresponds to UniProt isoform entries. Use this to
    document isoform-specific functions where different isoforms have distinct or even antagonistic biological
    activities. DEPRECATED: Use FunctionalIsoform instead for curated functional classes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["AlternativeProduct"]
    class_class_curie: ClassVar[str] = "gene_review:AlternativeProduct"
    class_name: ClassVar[str] = "AlternativeProduct"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.AlternativeProduct

    id: Union[str, AlternativeProductId] = None
    name: Optional[str] = None
    sequence_note: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlternativeProductId):
            self.id = AlternativeProductId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.sequence_note is not None and not isinstance(self.sequence_note, str):
            self.sequence_note = str(self.sequence_note)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalIsoform(YAMLRoot):
    """
    A curated functional isoform class. Unlike AlternativeProduct (which maps 1:1 to UniProt isoforms), this captures
    FUNCTIONALLY RELEVANT distinctions that may: - Group multiple UniProt isoforms into a functional class (e.g., WT1
    +KTS isoforms) - Represent cleavage products from polyproteins (e.g., POMC peptides) - Describe modification
    states or conformational variants Only create entries when there ARE functionally distinct forms worth
    documenting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["FunctionalIsoform"]
    class_class_curie: ClassVar[str] = "gene_review:FunctionalIsoform"
    class_name: ClassVar[str] = "FunctionalIsoform"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.FunctionalIsoform

    id: Union[str, FunctionalIsoformId] = None
    name: str = None
    type: Union[str, "FunctionalIsoformTypeEnum"] = None
    description: str = None
    maps_to: Optional[Union[Union[dict, "FunctionalIsoformMapping"], list[Union[dict, "FunctionalIsoformMapping"]]]] = empty_list()
    isoform_specific_terms: Optional[Union[dict[Union[str, TermId], Union[dict, "Term"]], list[Union[dict, "Term"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalIsoformId):
            self.id = FunctionalIsoformId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, FunctionalIsoformTypeEnum):
            self.type = FunctionalIsoformTypeEnum(self.type)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.maps_to, list):
            self.maps_to = [self.maps_to] if self.maps_to is not None else []
        self.maps_to = [v if isinstance(v, FunctionalIsoformMapping) else FunctionalIsoformMapping(**as_dict(v)) for v in self.maps_to]

        self._normalize_inlined_as_list(slot_name="isoform_specific_terms", slot_type=Term, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalIsoformMapping(YAMLRoot):
    """
    A mapping from a functional isoform class to underlying UniProt identifiers. Allows grouping multiple UniProt
    isoforms or chains into a single functional class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["FunctionalIsoformMapping"]
    class_class_curie: ClassVar[str] = "gene_review:FunctionalIsoformMapping"
    class_name: ClassVar[str] = "FunctionalIsoformMapping"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.FunctionalIsoformMapping

    type: Union[str, "FunctionalIsoformMappingTypeEnum"] = None
    ids: Union[str, list[str]] = None
    residues: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, FunctionalIsoformMappingTypeEnum):
            self.type = FunctionalIsoformMappingTypeEnum(self.type)

        if self._is_empty(self.ids):
            self.MissingRequiredField("ids")
        if not isinstance(self.ids, list):
            self.ids = [self.ids] if self.ids is not None else []
        self.ids = [v if isinstance(v, str) else str(v) for v in self.ids]

        if self.residues is not None and not isinstance(self.residues, str):
            self.residues = str(self.residues)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Term(YAMLRoot):
    """
    A term in a specific ontology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Term"]
    class_class_curie: ClassVar[str] = "gene_review:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Term

    id: Union[str, TermId] = None
    label: str = None
    description: Optional[str] = None
    ontology: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TermId):
            self.id = TermId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology is not None and not isinstance(self.ontology, str):
            self.ontology = str(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reference(YAMLRoot):
    """
    A reference is a published text that describes a finding or a method. References might be formal publications
    (where the ID is a PMID), or for methods, a GO_REF. Additionally, a reference to a local ad-hoc analysis or review
    can be made by using the `file:` prefix.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Reference"]
    class_class_curie: ClassVar[str] = "gene_review:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Reference

    id: Union[str, ReferenceId] = None
    title: str = None
    findings: Optional[Union[Union[dict, "Finding"], list[Union[dict, "Finding"]]]] = empty_list()
    is_invalid: Optional[Union[bool, Bool]] = None
    full_text_unavailable: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReferenceId):
            self.id = ReferenceId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.findings, list):
            self.findings = [self.findings] if self.findings is not None else []
        self.findings = [v if isinstance(v, Finding) else Finding(**as_dict(v)) for v in self.findings]

        if self.is_invalid is not None and not isinstance(self.is_invalid, Bool):
            self.is_invalid = Bool(self.is_invalid)

        if self.full_text_unavailable is not None and not isinstance(self.full_text_unavailable, Bool):
            self.full_text_unavailable = Bool(self.full_text_unavailable)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Finding(YAMLRoot):
    """
    A finding is a statement about a gene, which is supported by a reference. Similar to "comments" in uniprot
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Finding"]
    class_class_curie: ClassVar[str] = "gene_review:Finding"
    class_name: ClassVar[str] = "Finding"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Finding

    statement: Optional[str] = None
    supporting_text: Optional[str] = None
    full_text_unavailable: Optional[Union[bool, Bool]] = None
    reference_section_type: Optional[Union[str, "ManuscriptSection"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.statement is not None and not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

        if self.full_text_unavailable is not None and not isinstance(self.full_text_unavailable, Bool):
            self.full_text_unavailable = Bool(self.full_text_unavailable)

        if self.reference_section_type is not None and not isinstance(self.reference_section_type, ManuscriptSection):
            self.reference_section_type = ManuscriptSection(self.reference_section_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingTextInReference(YAMLRoot):
    """
    A supporting text in a reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["SupportingTextInReference"]
    class_class_curie: ClassVar[str] = "gene_review:SupportingTextInReference"
    class_name: ClassVar[str] = "SupportingTextInReference"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.SupportingTextInReference

    reference_id: Union[str, ReferenceId] = None
    supporting_text: Optional[str] = None
    supporting_text_fulltext: Optional[str] = None
    full_text_unavailable: Optional[Union[bool, Bool]] = None
    reference_section_type: Optional[Union[str, "ManuscriptSection"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_id):
            self.MissingRequiredField("reference_id")
        if not isinstance(self.reference_id, ReferenceId):
            self.reference_id = ReferenceId(self.reference_id)

        if self.supporting_text is not None and not isinstance(self.supporting_text, str):
            self.supporting_text = str(self.supporting_text)

        if self.supporting_text_fulltext is not None and not isinstance(self.supporting_text_fulltext, str):
            self.supporting_text_fulltext = str(self.supporting_text_fulltext)

        if self.full_text_unavailable is not None and not isinstance(self.full_text_unavailable, Bool):
            self.full_text_unavailable = Bool(self.full_text_unavailable)

        if self.reference_section_type is not None and not isinstance(self.reference_section_type, ManuscriptSection):
            self.reference_section_type = ManuscriptSection(self.reference_section_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExistingAnnotation(YAMLRoot):
    """
    An existing annotation from the GO database, plus a review of the annotation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ExistingAnnotation"]
    class_class_curie: ClassVar[str] = "gene_review:ExistingAnnotation"
    class_name: ClassVar[str] = "ExistingAnnotation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ExistingAnnotation

    evidence_type: Union[str, "EvidenceType"] = None
    term: Optional[Union[dict, Term]] = None
    extensions: Optional[Union[Union[dict, "AnnotationExtension"], list[Union[dict, "AnnotationExtension"]]]] = empty_list()
    negated: Optional[Union[bool, Bool]] = None
    original_reference_id: Optional[Union[str, ReferenceId]] = None
    retired: Optional[Union[bool, Bool]] = None
    isoform: Optional[str] = None
    supporting_entities: Optional[Union[str, list[str]]] = empty_list()
    review: Optional[Union[dict, "Review"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.evidence_type):
            self.MissingRequiredField("evidence_type")
        if not isinstance(self.evidence_type, EvidenceType):
            self.evidence_type = EvidenceType(self.evidence_type)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        self._normalize_inlined_as_dict(slot_name="extensions", slot_type=AnnotationExtension, key_name="predicate", keyed=False)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.original_reference_id is not None and not isinstance(self.original_reference_id, ReferenceId):
            self.original_reference_id = ReferenceId(self.original_reference_id)

        if self.retired is not None and not isinstance(self.retired, Bool):
            self.retired = Bool(self.retired)

        if self.isoform is not None and not isinstance(self.isoform, str):
            self.isoform = str(self.isoform)

        if not isinstance(self.supporting_entities, list):
            self.supporting_entities = [self.supporting_entities] if self.supporting_entities is not None else []
        self.supporting_entities = [v if isinstance(v, str) else str(v) for v in self.supporting_entities]

        if self.review is not None and not isinstance(self.review, Review):
            self.review = Review(**as_dict(self.review))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Review(YAMLRoot):
    """
    A review of an existing annotation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Review"]
    class_class_curie: ClassVar[str] = "gene_review:Review"
    class_name: ClassVar[str] = "Review"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Review

    action: Union[str, "ActionEnum"] = None
    summary: Optional[str] = None
    reason: Optional[str] = None
    proposed_replacement_terms: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    additional_reference_ids: Optional[Union[Union[str, ReferenceId], list[Union[str, ReferenceId]]]] = empty_list()
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, ActionEnum):
            self.action = ActionEnum(self.action)

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if self.reason is not None and not isinstance(self.reason, str):
            self.reason = str(self.reason)

        self._normalize_inlined_as_list(slot_name="proposed_replacement_terms", slot_type=Term, key_name="id", keyed=True)

        if not isinstance(self.additional_reference_ids, list):
            self.additional_reference_ids = [self.additional_reference_ids] if self.additional_reference_ids is not None else []
        self.additional_reference_ids = [v if isinstance(v, ReferenceId) else ReferenceId(v) for v in self.additional_reference_ids]

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoreFunction(YAMLRoot):
    """
    A core function is a GO-CAM-like annotation of the core evolved functions of a gene. This is a synthesis of the
    reviewed core annotations, brought together into a unified GO-CAM-like representation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["CoreFunction"]
    class_class_curie: ClassVar[str] = "gene_review:CoreFunction"
    class_name: ClassVar[str] = "CoreFunction"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.CoreFunction

    molecular_function: Union[dict, Term] = None
    description: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()
    directly_involved_in: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    locations: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    anatomical_locations: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    substrates: Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]] = empty_dict()
    in_complex: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.molecular_function):
            self.MissingRequiredField("molecular_function")
        if not isinstance(self.molecular_function, Term):
            self.molecular_function = Term(**as_dict(self.molecular_function))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="directly_involved_in", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="anatomical_locations", slot_type=Term, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="substrates", slot_type=Term, key_name="id", keyed=True)

        if self.in_complex is not None and not isinstance(self.in_complex, Term):
            self.in_complex = Term(**as_dict(self.in_complex))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnnotationExtension(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["AnnotationExtension"]
    class_class_curie: ClassVar[str] = "gene_review:AnnotationExtension"
    class_name: ClassVar[str] = "AnnotationExtension"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.AnnotationExtension

    predicate: str = None
    term: Optional[Union[dict, Term]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.term is not None and not isinstance(self.term, Term):
            self.term = Term(**as_dict(self.term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermMapping(YAMLRoot):
    """
    A mapping between the proposed term and an equivalent term in another ontology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["TermMapping"]
    class_class_curie: ClassVar[str] = "gene_review:TermMapping"
    class_name: ClassVar[str] = "TermMapping"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.TermMapping

    predicate: str = None
    target_term: Union[dict, Term] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.target_term):
            self.MissingRequiredField("target_term")
        if not isinstance(self.target_term, Term):
            self.target_term = Term(**as_dict(self.target_term))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProposedOntologyTerm(YAMLRoot):
    """
    A proposed new ontology term that should exist but doesn't currently
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ProposedOntologyTerm"]
    class_class_curie: ClassVar[str] = "gene_review:ProposedOntologyTerm"
    class_name: ClassVar[str] = "ProposedOntologyTerm"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ProposedOntologyTerm

    proposed_name: str = None
    proposed_definition: str = None
    justification: Optional[str] = None
    proposed_parent: Optional[Union[dict, Term]] = None
    proposed_mappings: Optional[Union[Union[dict, TermMapping], list[Union[dict, TermMapping]]]] = empty_list()
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.proposed_name):
            self.MissingRequiredField("proposed_name")
        if not isinstance(self.proposed_name, str):
            self.proposed_name = str(self.proposed_name)

        if self._is_empty(self.proposed_definition):
            self.MissingRequiredField("proposed_definition")
        if not isinstance(self.proposed_definition, str):
            self.proposed_definition = str(self.proposed_definition)

        if self.justification is not None and not isinstance(self.justification, str):
            self.justification = str(self.justification)

        if self.proposed_parent is not None and not isinstance(self.proposed_parent, Term):
            self.proposed_parent = Term(**as_dict(self.proposed_parent))

        if not isinstance(self.proposed_mappings, list):
            self.proposed_mappings = [self.proposed_mappings] if self.proposed_mappings is not None else []
        self.proposed_mappings = [v if isinstance(v, TermMapping) else TermMapping(**as_dict(v)) for v in self.proposed_mappings]

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(YAMLRoot):
    """
    A suggested experiment to answer a question about the gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Experiment"]
    class_class_curie: ClassVar[str] = "gene_review:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Experiment

    description: str = None
    hypothesis: Optional[str] = None
    experiment_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.hypothesis is not None and not isinstance(self.hypothesis, str):
            self.hypothesis = str(self.hypothesis)

        if self.experiment_type is not None and not isinstance(self.experiment_type, str):
            self.experiment_type = str(self.experiment_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Question(YAMLRoot):
    """
    A question to be answered about the gene
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["Question"]
    class_class_curie: ClassVar[str] = "gene_review:Question"
    class_name: ClassVar[str] = "Question"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.Question

    question: str = None
    experts: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.question):
            self.MissingRequiredField("question")
        if not isinstance(self.question, str):
            self.question = str(self.question)

        if not isinstance(self.experts, list):
            self.experts = [self.experts] if self.experts is not None else []
        self.experts = [v if isinstance(v, str) else str(v) for v in self.experts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleReview(YAMLRoot):
    """
    A review of a UniProt annotation rule (ARBA or UniRule). Each review covers ONE rule and assesses its quality,
    literature support, and biological appropriateness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleReview"]
    class_class_curie: ClassVar[str] = "gene_review:RuleReview"
    class_name: ClassVar[str] = "RuleReview"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleReview

    id: Union[str, RuleReviewId] = None
    rule_type: Union[str, "RuleTypeEnum"] = None
    rule: Union[dict, "EmbeddedRule"] = None
    action: Union[str, "RuleActionEnum"] = None
    description: Optional[str] = None
    references: Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]] = empty_dict()
    status: Optional[Union[str, "RuleReviewStatusEnum"]] = None
    review_summary: Optional[str] = None
    action_rationale: Optional[str] = None
    suggested_modifications: Optional[Union[str, list[str]]] = empty_list()
    parsimony: Optional[Union[dict, "ParsimonyAssessment"]] = None
    literature_support: Optional[Union[dict, "LiteratureSupportAssessment"]] = None
    condition_overlap: Optional[Union[dict, "ConditionOverlapAssessment"]] = None
    go_specificity: Optional[Union[dict, "GOSpecificityAssessment"]] = None
    taxonomic_scope: Optional[Union[dict, "TaxonomicScopeAssessment"]] = None
    confidence: Optional[float] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleReviewId):
            self.id = RuleReviewId(self.id)

        if self._is_empty(self.rule_type):
            self.MissingRequiredField("rule_type")
        if not isinstance(self.rule_type, RuleTypeEnum):
            self.rule_type = RuleTypeEnum(self.rule_type)

        if self._is_empty(self.rule):
            self.MissingRequiredField("rule")
        if not isinstance(self.rule, EmbeddedRule):
            self.rule = EmbeddedRule(**as_dict(self.rule))

        if self._is_empty(self.action):
            self.MissingRequiredField("action")
        if not isinstance(self.action, RuleActionEnum):
            self.action = RuleActionEnum(self.action)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="references", slot_type=Reference, key_name="id", keyed=True)

        if self.status is not None and not isinstance(self.status, RuleReviewStatusEnum):
            self.status = RuleReviewStatusEnum(self.status)

        if self.review_summary is not None and not isinstance(self.review_summary, str):
            self.review_summary = str(self.review_summary)

        if self.action_rationale is not None and not isinstance(self.action_rationale, str):
            self.action_rationale = str(self.action_rationale)

        if not isinstance(self.suggested_modifications, list):
            self.suggested_modifications = [self.suggested_modifications] if self.suggested_modifications is not None else []
        self.suggested_modifications = [v if isinstance(v, str) else str(v) for v in self.suggested_modifications]

        if self.parsimony is not None and not isinstance(self.parsimony, ParsimonyAssessment):
            self.parsimony = ParsimonyAssessment(**as_dict(self.parsimony))

        if self.literature_support is not None and not isinstance(self.literature_support, LiteratureSupportAssessment):
            self.literature_support = LiteratureSupportAssessment(**as_dict(self.literature_support))

        if self.condition_overlap is not None and not isinstance(self.condition_overlap, ConditionOverlapAssessment):
            self.condition_overlap = ConditionOverlapAssessment(**as_dict(self.condition_overlap))

        if self.go_specificity is not None and not isinstance(self.go_specificity, GOSpecificityAssessment):
            self.go_specificity = GOSpecificityAssessment(**as_dict(self.go_specificity))

        if self.taxonomic_scope is not None and not isinstance(self.taxonomic_scope, TaxonomicScopeAssessment):
            self.taxonomic_scope = TaxonomicScopeAssessment(**as_dict(self.taxonomic_scope))

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmbeddedRule(YAMLRoot):
    """
    An embedded representation of an ARBA or UniRule for storage in YAML. Captures the essential structure: conditions
    (antecedent) and GO annotations (consequent).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["EmbeddedRule"]
    class_class_curie: ClassVar[str] = "gene_review:EmbeddedRule"
    class_name: ClassVar[str] = "EmbeddedRule"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.EmbeddedRule

    rule_id: str = None
    condition_sets: Union[Union[dict, "RuleConditionSet"], list[Union[dict, "RuleConditionSet"]]] = None
    entries: Union[dict[Union[str, RuleReviewEntryId], Union[dict, "RuleReviewEntry"]], list[Union[dict, "RuleReviewEntry"]]] = empty_dict()
    go_annotations: Optional[Union[Union[dict, "RuleGOAnnotation"], list[Union[dict, "RuleGOAnnotation"]]]] = empty_list()
    ipr2go_redundancy: Optional[Union[dict, "InterPro2GORedundancy"]] = None
    reviewed_protein_count: Optional[int] = None
    unreviewed_protein_count: Optional[int] = None
    created_date: Optional[str] = None
    modified_date: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rule_id):
            self.MissingRequiredField("rule_id")
        if not isinstance(self.rule_id, str):
            self.rule_id = str(self.rule_id)

        if self._is_empty(self.condition_sets):
            self.MissingRequiredField("condition_sets")
        if not isinstance(self.condition_sets, list):
            self.condition_sets = [self.condition_sets] if self.condition_sets is not None else []
        self.condition_sets = [v if isinstance(v, RuleConditionSet) else RuleConditionSet(**as_dict(v)) for v in self.condition_sets]

        if self._is_empty(self.entries):
            self.MissingRequiredField("entries")
        self._normalize_inlined_as_list(slot_name="entries", slot_type=RuleReviewEntry, key_name="id", keyed=True)

        if not isinstance(self.go_annotations, list):
            self.go_annotations = [self.go_annotations] if self.go_annotations is not None else []
        self.go_annotations = [v if isinstance(v, RuleGOAnnotation) else RuleGOAnnotation(**as_dict(v)) for v in self.go_annotations]

        if self.ipr2go_redundancy is not None and not isinstance(self.ipr2go_redundancy, InterPro2GORedundancy):
            self.ipr2go_redundancy = InterPro2GORedundancy(**as_dict(self.ipr2go_redundancy))

        if self.reviewed_protein_count is not None and not isinstance(self.reviewed_protein_count, int):
            self.reviewed_protein_count = int(self.reviewed_protein_count)

        if self.unreviewed_protein_count is not None and not isinstance(self.unreviewed_protein_count, int):
            self.unreviewed_protein_count = int(self.unreviewed_protein_count)

        if self.created_date is not None and not isinstance(self.created_date, str):
            self.created_date = str(self.created_date)

        if self.modified_date is not None and not isinstance(self.modified_date, str):
            self.modified_date = str(self.modified_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleConditionSet(YAMLRoot):
    """
    A set of conditions that must ALL be true (conjunction/AND). Multiple condition sets in a rule are OR-ed together
    (disjunction).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleConditionSet"]
    class_class_curie: ClassVar[str] = "gene_review:RuleConditionSet"
    class_name: ClassVar[str] = "RuleConditionSet"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleConditionSet

    number: int = None
    conditions: Union[Union[dict, "RuleCondition"], list[Union[dict, "RuleCondition"]]] = None
    notes: Optional[str] = None
    pairwise_overlap: Optional[Union[Union[dict, "PairwiseOverlap"], list[Union[dict, "PairwiseOverlap"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number):
            self.MissingRequiredField("number")
        if not isinstance(self.number, int):
            self.number = int(self.number)

        if self._is_empty(self.conditions):
            self.MissingRequiredField("conditions")
        if not isinstance(self.conditions, list):
            self.conditions = [self.conditions] if self.conditions is not None else []
        self.conditions = [v if isinstance(v, RuleCondition) else RuleCondition(**as_dict(v)) for v in self.conditions]

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if not isinstance(self.pairwise_overlap, list):
            self.pairwise_overlap = [self.pairwise_overlap] if self.pairwise_overlap is not None else []
        self.pairwise_overlap = [v if isinstance(v, PairwiseOverlap) else PairwiseOverlap(**as_dict(v)) for v in self.pairwise_overlap]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleCondition(YAMLRoot):
    """
    A single condition in a rule antecedent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleCondition"]
    class_class_curie: ClassVar[str] = "gene_review:RuleCondition"
    class_name: ClassVar[str] = "RuleCondition"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleCondition

    condition_type: Union[str, "ConditionTypeEnum"] = None
    value: str = None
    curie: Optional[str] = None
    label: Optional[str] = None
    interpro_type: Optional[Union[str, "InterProTypeEnum"]] = None
    negated: Optional[Union[bool, Bool]] = None
    protein_count: Optional[int] = None
    protein_database: Optional[Union[str, "ProteinDatabaseEnum"]] = None
    uniqueness_score: Optional[float] = None
    sample_proteins: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_type):
            self.MissingRequiredField("condition_type")
        if not isinstance(self.condition_type, ConditionTypeEnum):
            self.condition_type = ConditionTypeEnum(self.condition_type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.interpro_type is not None and not isinstance(self.interpro_type, InterProTypeEnum):
            self.interpro_type = InterProTypeEnum(self.interpro_type)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if self.protein_count is not None and not isinstance(self.protein_count, int):
            self.protein_count = int(self.protein_count)

        if self.protein_database is not None and not isinstance(self.protein_database, ProteinDatabaseEnum):
            self.protein_database = ProteinDatabaseEnum(self.protein_database)

        if self.uniqueness_score is not None and not isinstance(self.uniqueness_score, float):
            self.uniqueness_score = float(self.uniqueness_score)

        if not isinstance(self.sample_proteins, list):
            self.sample_proteins = [self.sample_proteins] if self.sample_proteins is not None else []
        self.sample_proteins = [v if isinstance(v, str) else str(v) for v in self.sample_proteins]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleGOAnnotation(YAMLRoot):
    """
    A GO annotation produced by the rule
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleGOAnnotation"]
    class_class_curie: ClassVar[str] = "gene_review:RuleGOAnnotation"
    class_name: ClassVar[str] = "RuleGOAnnotation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleGOAnnotation

    go_id: str = None
    go_label: Optional[str] = None
    aspect: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.go_id):
            self.MissingRequiredField("go_id")
        if not isinstance(self.go_id, str):
            self.go_id = str(self.go_id)

        if self.go_label is not None and not isinstance(self.go_label, str):
            self.go_label = str(self.go_label)

        if self.aspect is not None and not isinstance(self.aspect, str):
            self.aspect = str(self.aspect)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PairwiseOverlap(YAMLRoot):
    """
    Overlap statistics between two domain conditions (InterPro, FunFam, etc.) in the same condition set. Provides set
    difference metrics to measure uniqueness and redundancy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["PairwiseOverlap"]
    class_class_curie: ClassVar[str] = "gene_review:PairwiseOverlap"
    class_name: ClassVar[str] = "PairwiseOverlap"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.PairwiseOverlap

    condition_a: str = None
    condition_b: str = None
    protein_database: Union[str, "ProteinDatabaseEnum"] = None
    count_a: int = None
    count_b: int = None
    intersection_count: int = None
    a_minus_b_count: int = None
    b_minus_a_count: int = None
    jaccard_similarity: float = None
    containment_a_in_b: float = None
    containment_b_in_a: float = None
    condition_a_label: Optional[str] = None
    condition_b_label: Optional[str] = None
    interpretation: Optional[Union[str, "OverlapInterpretationEnum"]] = None
    condition_a_in_sets: Optional[Union[int, list[int]]] = empty_list()
    condition_b_in_sets: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.condition_a):
            self.MissingRequiredField("condition_a")
        if not isinstance(self.condition_a, str):
            self.condition_a = str(self.condition_a)

        if self._is_empty(self.condition_b):
            self.MissingRequiredField("condition_b")
        if not isinstance(self.condition_b, str):
            self.condition_b = str(self.condition_b)

        if self._is_empty(self.protein_database):
            self.MissingRequiredField("protein_database")
        if not isinstance(self.protein_database, ProteinDatabaseEnum):
            self.protein_database = ProteinDatabaseEnum(self.protein_database)

        if self._is_empty(self.count_a):
            self.MissingRequiredField("count_a")
        if not isinstance(self.count_a, int):
            self.count_a = int(self.count_a)

        if self._is_empty(self.count_b):
            self.MissingRequiredField("count_b")
        if not isinstance(self.count_b, int):
            self.count_b = int(self.count_b)

        if self._is_empty(self.intersection_count):
            self.MissingRequiredField("intersection_count")
        if not isinstance(self.intersection_count, int):
            self.intersection_count = int(self.intersection_count)

        if self._is_empty(self.a_minus_b_count):
            self.MissingRequiredField("a_minus_b_count")
        if not isinstance(self.a_minus_b_count, int):
            self.a_minus_b_count = int(self.a_minus_b_count)

        if self._is_empty(self.b_minus_a_count):
            self.MissingRequiredField("b_minus_a_count")
        if not isinstance(self.b_minus_a_count, int):
            self.b_minus_a_count = int(self.b_minus_a_count)

        if self._is_empty(self.jaccard_similarity):
            self.MissingRequiredField("jaccard_similarity")
        if not isinstance(self.jaccard_similarity, float):
            self.jaccard_similarity = float(self.jaccard_similarity)

        if self._is_empty(self.containment_a_in_b):
            self.MissingRequiredField("containment_a_in_b")
        if not isinstance(self.containment_a_in_b, float):
            self.containment_a_in_b = float(self.containment_a_in_b)

        if self._is_empty(self.containment_b_in_a):
            self.MissingRequiredField("containment_b_in_a")
        if not isinstance(self.containment_b_in_a, float):
            self.containment_b_in_a = float(self.containment_b_in_a)

        if self.condition_a_label is not None and not isinstance(self.condition_a_label, str):
            self.condition_a_label = str(self.condition_a_label)

        if self.condition_b_label is not None and not isinstance(self.condition_b_label, str):
            self.condition_b_label = str(self.condition_b_label)

        if self.interpretation is not None and not isinstance(self.interpretation, OverlapInterpretationEnum):
            self.interpretation = OverlapInterpretationEnum(self.interpretation)

        if not isinstance(self.condition_a_in_sets, list):
            self.condition_a_in_sets = [self.condition_a_in_sets] if self.condition_a_in_sets is not None else []
        self.condition_a_in_sets = [v if isinstance(v, int) else int(v) for v in self.condition_a_in_sets]

        if not isinstance(self.condition_b_in_sets, list):
            self.condition_b_in_sets = [self.condition_b_in_sets] if self.condition_b_in_sets is not None else []
        self.condition_b_in_sets = [v if isinstance(v, int) else int(v) for v in self.condition_b_in_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleReviewEntry(YAMLRoot):
    """
    An entity in the rule - either a domain/family condition or a GO term target. Each entry tracks its relationships
    (predictions, predicted-by, equivalence) to other entries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RuleReviewEntry"]
    class_class_curie: ClassVar[str] = "gene_review:RuleReviewEntry"
    class_name: ClassVar[str] = "RuleReviewEntry"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RuleReviewEntry

    id: Union[str, RuleReviewEntryId] = None
    type: Union[str, "EntryTypeEnum"] = None
    label: Optional[str] = None
    appears_in_condition_sets: Optional[Union[int, list[int]]] = empty_list()
    protein_count: Optional[int] = None
    source: Optional[str] = None
    asserted_predicted_go_terms: Optional[Union[str, list[str]]] = empty_list()
    related_entries: Optional[Union[Union[dict, "RelatedEntry"], list[Union[dict, "RelatedEntry"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleReviewEntryId):
            self.id = RuleReviewEntryId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, EntryTypeEnum):
            self.type = EntryTypeEnum(self.type)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.appears_in_condition_sets, list):
            self.appears_in_condition_sets = [self.appears_in_condition_sets] if self.appears_in_condition_sets is not None else []
        self.appears_in_condition_sets = [v if isinstance(v, int) else int(v) for v in self.appears_in_condition_sets]

        if self.protein_count is not None and not isinstance(self.protein_count, int):
            self.protein_count = int(self.protein_count)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if not isinstance(self.asserted_predicted_go_terms, list):
            self.asserted_predicted_go_terms = [self.asserted_predicted_go_terms] if self.asserted_predicted_go_terms is not None else []
        self.asserted_predicted_go_terms = [v if isinstance(v, str) else str(v) for v in self.asserted_predicted_go_terms]

        if not isinstance(self.related_entries, list):
            self.related_entries = [self.related_entries] if self.related_entries is not None else []
        self.related_entries = [v if isinstance(v, RelatedEntry) else RelatedEntry(**as_dict(v)) for v in self.related_entries]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedEntry(YAMLRoot):
    """
    A relationship from this entry to another entry in the rule. Categorized as PREDICTS (this → other), PREDICTED_BY
    (other → this), or EQUIV (bidirectional).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RelatedEntry"]
    class_class_curie: ClassVar[str] = "gene_review:RelatedEntry"
    class_name: ClassVar[str] = "RelatedEntry"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RelatedEntry

    relationship: Union[str, "EntryRelationshipEnum"] = None
    target_id: str = None
    containment: Optional[float] = None
    jaccard_similarity: Optional[float] = None
    intersection_count: Optional[int] = None
    exclusive_count: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.relationship):
            self.MissingRequiredField("relationship")
        if not isinstance(self.relationship, EntryRelationshipEnum):
            self.relationship = EntryRelationshipEnum(self.relationship)

        if self._is_empty(self.target_id):
            self.MissingRequiredField("target_id")
        if not isinstance(self.target_id, str):
            self.target_id = str(self.target_id)

        if self.containment is not None and not isinstance(self.containment, float):
            self.containment = float(self.containment)

        if self.jaccard_similarity is not None and not isinstance(self.jaccard_similarity, float):
            self.jaccard_similarity = float(self.jaccard_similarity)

        if self.intersection_count is not None and not isinstance(self.intersection_count, int):
            self.intersection_count = int(self.intersection_count)

        if self.exclusive_count is not None and not isinstance(self.exclusive_count, int):
            self.exclusive_count = int(self.exclusive_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterPro2GORedundancy(YAMLRoot):
    """
    Analysis of whether rule GO annotations are redundant with existing InterPro2GO mappings from the GO Consortium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["InterPro2GORedundancy"]
    class_class_curie: ClassVar[str] = "gene_review:InterPro2GORedundancy"
    class_name: ClassVar[str] = "InterPro2GORedundancy"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.InterPro2GORedundancy

    redundant_annotations: Optional[Union[Union[dict, "RedundantAnnotation"], list[Union[dict, "RedundantAnnotation"]]]] = empty_list()
    novel_annotations: Optional[Union[str, list[str]]] = empty_list()
    summary: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.redundant_annotations, list):
            self.redundant_annotations = [self.redundant_annotations] if self.redundant_annotations is not None else []
        self.redundant_annotations = [v if isinstance(v, RedundantAnnotation) else RedundantAnnotation(**as_dict(v)) for v in self.redundant_annotations]

        if not isinstance(self.novel_annotations, list):
            self.novel_annotations = [self.novel_annotations] if self.novel_annotations is not None else []
        self.novel_annotations = [v if isinstance(v, str) else str(v) for v in self.novel_annotations]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RedundantAnnotation(YAMLRoot):
    """
    A GO annotation that is redundant with an existing InterPro2GO mapping
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["RedundantAnnotation"]
    class_class_curie: ClassVar[str] = "gene_review:RedundantAnnotation"
    class_name: ClassVar[str] = "RedundantAnnotation"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.RedundantAnnotation

    go_id: str = None
    interpro_source: str = None
    go_label: Optional[str] = None
    interpro_label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.go_id):
            self.MissingRequiredField("go_id")
        if not isinstance(self.go_id, str):
            self.go_id = str(self.go_id)

        if self._is_empty(self.interpro_source):
            self.MissingRequiredField("interpro_source")
        if not isinstance(self.interpro_source, str):
            self.interpro_source = str(self.interpro_source)

        if self.go_label is not None and not isinstance(self.go_label, str):
            self.go_label = str(self.go_label)

        if self.interpro_label is not None and not isinstance(self.interpro_label, str):
            self.interpro_label = str(self.interpro_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParsimonyAssessment(YAMLRoot):
    """
    Assessment of rule parsimony (simplicity vs complexity)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ParsimonyAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:ParsimonyAssessment"
    class_name: ClassVar[str] = "ParsimonyAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ParsimonyAssessment

    assessment: Union[str, "ParsimonyEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, ParsimonyEnum):
            self.assessment = ParsimonyEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LiteratureSupportAssessment(YAMLRoot):
    """
    Assessment of literature support for the rule
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["LiteratureSupportAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:LiteratureSupportAssessment"
    class_name: ClassVar[str] = "LiteratureSupportAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.LiteratureSupportAssessment

    assessment: Union[str, "LiteratureSupportEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, LiteratureSupportEnum):
            self.assessment = LiteratureSupportEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConditionOverlapAssessment(YAMLRoot):
    """
    Assessment of overlap between rule conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["ConditionOverlapAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:ConditionOverlapAssessment"
    class_name: ClassVar[str] = "ConditionOverlapAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.ConditionOverlapAssessment

    assessment: Union[str, "OverlapEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, OverlapEnum):
            self.assessment = OverlapEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GOSpecificityAssessment(YAMLRoot):
    """
    Assessment of GO term specificity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["GOSpecificityAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:GOSpecificityAssessment"
    class_name: ClassVar[str] = "GOSpecificityAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.GOSpecificityAssessment

    assessment: Union[str, "SpecificityEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, SpecificityEnum):
            self.assessment = SpecificityEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomicScopeAssessment(YAMLRoot):
    """
    Assessment of taxonomic restriction appropriateness
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GENE_REVIEW["TaxonomicScopeAssessment"]
    class_class_curie: ClassVar[str] = "gene_review:TaxonomicScopeAssessment"
    class_name: ClassVar[str] = "TaxonomicScopeAssessment"
    class_model_uri: ClassVar[URIRef] = GENE_REVIEW.TaxonomicScopeAssessment

    assessment: Union[str, "TaxonomicScopeEnum"] = None
    notes: Optional[str] = None
    supported_by: Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment):
            self.MissingRequiredField("assessment")
        if not isinstance(self.assessment, TaxonomicScopeEnum):
            self.assessment = TaxonomicScopeEnum(self.assessment)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        self._normalize_inlined_as_dict(slot_name="supported_by", slot_type=SupportingTextInReference, key_name="reference_id", keyed=False)

        super().__post_init__(**kwargs)


# Enumerations
class EvidenceType(EnumDefinitionImpl):
    """
    Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms
    """
    EXP = PermissibleValue(
        text="EXP",
        description="Inferred from Experiment",
        meaning=ECO["0000269"])
    IDA = PermissibleValue(
        text="IDA",
        description="Inferred from Direct Assay",
        meaning=ECO["0000314"])
    IPI = PermissibleValue(
        text="IPI",
        description="Inferred from Physical Interaction",
        meaning=ECO["0000353"])
    IMP = PermissibleValue(
        text="IMP",
        description="Inferred from Mutant Phenotype",
        meaning=ECO["0000315"])
    IGI = PermissibleValue(
        text="IGI",
        description="Inferred from Genetic Interaction",
        meaning=ECO["0000316"])
    IEP = PermissibleValue(
        text="IEP",
        description="Inferred from Expression Pattern",
        meaning=ECO["0000270"])
    HTP = PermissibleValue(
        text="HTP",
        description="Inferred from High Throughput Experiment",
        meaning=ECO["0006056"])
    HDA = PermissibleValue(
        text="HDA",
        description="Inferred from High Throughput Direct Assay",
        meaning=ECO["0007005"])
    HMP = PermissibleValue(
        text="HMP",
        description="Inferred from High Throughput Mutant Phenotype",
        meaning=ECO["0007001"])
    HGI = PermissibleValue(
        text="HGI",
        description="Inferred from High Throughput Genetic Interaction",
        meaning=ECO["0007003"])
    HEP = PermissibleValue(
        text="HEP",
        description="Inferred from High Throughput Expression Pattern",
        meaning=ECO["0007007"])
    IBA = PermissibleValue(
        text="IBA",
        description="Inferred from Biological aspect of Ancestor",
        meaning=ECO["0000318"])
    IBD = PermissibleValue(
        text="IBD",
        description="Inferred from Biological aspect of Descendant",
        meaning=ECO["0000319"])
    IKR = PermissibleValue(
        text="IKR",
        description="Inferred from Key Residues",
        meaning=ECO["0000320"])
    IRD = PermissibleValue(
        text="IRD",
        description="Inferred from Rapid Divergence",
        meaning=ECO["0000321"])
    ISS = PermissibleValue(
        text="ISS",
        description="Inferred from Sequence or structural Similarity",
        meaning=ECO["0000250"])
    ISO = PermissibleValue(
        text="ISO",
        description="Inferred from Sequence Orthology",
        meaning=ECO["0000266"])
    ISA = PermissibleValue(
        text="ISA",
        description="Inferred from Sequence Alignment",
        meaning=ECO["0000247"])
    ISM = PermissibleValue(
        text="ISM",
        description="Inferred from Sequence Model",
        meaning=ECO["0000255"])
    IGC = PermissibleValue(
        text="IGC",
        description="Inferred from Genomic Context",
        meaning=ECO["0000317"])
    RCA = PermissibleValue(
        text="RCA",
        description="Inferred from Reviewed Computational Analysis",
        meaning=ECO["0000245"])
    TAS = PermissibleValue(
        text="TAS",
        description="Traceable Author Statement",
        meaning=ECO["0000304"])
    NAS = PermissibleValue(
        text="NAS",
        description="Non-traceable Author Statement",
        meaning=ECO["0000303"])
    IC = PermissibleValue(
        text="IC",
        description="Inferred by Curator",
        meaning=ECO["0000305"])
    ND = PermissibleValue(
        text="ND",
        description="No biological Data available",
        meaning=ECO["0000307"])
    IEA = PermissibleValue(
        text="IEA",
        description="Inferred from Electronic Annotation",
        meaning=ECO["0000501"])

    _defn = EnumDefinition(
        name="EvidenceType",
        description="Gene Ontology evidence codes mapped to Evidence and Conclusion Ontology (ECO) terms",
    )

class ActionEnum(EnumDefinitionImpl):

    ACCEPT = PermissibleValue(
        text="ACCEPT",
        description="""Accept the existing annotation as-is, no modifications, and retain as representing the core function of the gene""")
    KEEP_AS_NON_CORE = PermissibleValue(
        text="KEEP_AS_NON_CORE",
        description="""Keep the existing annotation as-is, but mark it as non-core. For pleiotropic genes, this may be the developmental processes, or other processes that are not the core function of the gene.""")
    REMOVE = PermissibleValue(
        text="REMOVE",
        description="Remove the existing annotation, as it is unlikely to be correct based on combined evidence")
    MODIFY = PermissibleValue(
        text="MODIFY",
        description="""The essence of the annotation is sound, but there are better terms to use (use in combination with proposed_replacement_terms). if the term is too general, then MODIFY should be used, with a proposed replacement term for the correct specific function. sometimes terms can also be overly specific and contorted, so in some cases you might want to generalize""")
    MARK_AS_OVER_ANNOTATED = PermissibleValue(
        text="MARK_AS_OVER_ANNOTATED",
        description="The term is not entirely wrong, but likely represents an over-annotation of the gene")
    UNDECIDED = PermissibleValue(
        text="UNDECIDED",
        description="""The annotation is not clear, and the reviewer is not sure what to do with it. ALWAYS USE THIS IF YOU ARE UNABLE TO ACCESS RELEVANT PUBLICATIONS""")
    PENDING = PermissibleValue(
        text="PENDING",
        description="The review entry is a stub, and the review has not been completed yet.")
    NEW = PermissibleValue(
        text="NEW",
        description="""This is a proposed annotation, not one that exists in the existing GO annotations. Use this to propose a new annotation not covered by the existing GO annotations. Use this conservatively, do not over-annotate, especially for biological process. Do not use for indirect or pleiotropic effects. Be sure you have good evidence, this can be from multiple sources.""")

    _defn = EnumDefinition(
        name="ActionEnum",
    )

class GOTermEnum(EnumDefinitionImpl):
    """
    A term in the GO ontology
    """
    _defn = EnumDefinition(
        name="GOTermEnum",
        description="A term in the GO ontology",
    )

class GOMolecularActivityEnum(EnumDefinitionImpl):
    """
    A molecular activity term in the GO ontology
    """
    _defn = EnumDefinition(
        name="GOMolecularActivityEnum",
        description="A molecular activity term in the GO ontology",
    )

class GOBiologicalProcessEnum(EnumDefinitionImpl):
    """
    A biological process term in the GO ontology
    """
    _defn = EnumDefinition(
        name="GOBiologicalProcessEnum",
        description="A biological process term in the GO ontology",
    )

class GOCellularLocationEnum(EnumDefinitionImpl):
    """
    A cellular location term in the GO ontology (excludes protein-containing complexes)
    """
    _defn = EnumDefinition(
        name="GOCellularLocationEnum",
        description="A cellular location term in the GO ontology (excludes protein-containing complexes)",
    )

class GOProteinContainingComplexEnum(EnumDefinitionImpl):
    """
    A protein-containing complex term in the GO ontology
    """
    _defn = EnumDefinition(
        name="GOProteinContainingComplexEnum",
        description="A protein-containing complex term in the GO ontology",
    )

class ROTermEnum(EnumDefinitionImpl):
    """
    A term in the relation ontology
    """
    _defn = EnumDefinition(
        name="ROTermEnum",
        description="A term in the relation ontology",
    )

class ProductTypeEnum(EnumDefinitionImpl):
    """
    Type of gene product
    """
    PROTEIN = PermissibleValue(
        text="PROTEIN",
        description="Protein-coding gene",
        meaning=SO["0001217"])
    MIRNA = PermissibleValue(
        text="MIRNA",
        description="microRNA",
        meaning=SO["0000276"])
    LNCRNA = PermissibleValue(
        text="LNCRNA",
        description="Long non-coding RNA",
        meaning=SO["0001877"])
    SNORNA = PermissibleValue(
        text="SNORNA",
        description="Small nucleolar RNA",
        meaning=SO["0000275"])
    SNRNA = PermissibleValue(
        text="SNRNA",
        description="Small nuclear RNA",
        meaning=SO["0000274"])
    TRNA = PermissibleValue(
        text="TRNA",
        description="Transfer RNA",
        meaning=SO["0000253"])
    RRNA = PermissibleValue(
        text="RRNA",
        description="Ribosomal RNA",
        meaning=SO["0000252"])
    PIRNA = PermissibleValue(
        text="PIRNA",
        description="PIWI-interacting RNA",
        meaning=SO["0001035"])
    ANTISENSE_RNA = PermissibleValue(
        text="ANTISENSE_RNA",
        description="Antisense RNA",
        meaning=SO["0000644"])
    PSEUDOGENE = PermissibleValue(
        text="PSEUDOGENE",
        description="Pseudogene",
        meaning=SO["0000336"])
    OTHER_NCRNA = PermissibleValue(
        text="OTHER_NCRNA",
        description="Other non-coding RNA",
        meaning=SO["0000655"])

    _defn = EnumDefinition(
        name="ProductTypeEnum",
        description="Type of gene product",
    )

class GeneReviewStatusEnum(EnumDefinitionImpl):
    """
    Status of the gene review process
    """
    INITIALIZED = PermissibleValue(
        text="INITIALIZED",
        description="All annotations have action PENDING - review has been initialized but not started")
    IN_PROGRESS = PermissibleValue(
        text="IN_PROGRESS",
        description="""At least one annotation is PENDING and at least one annotation is not PENDING - review is underway""")
    DRAFT = PermissibleValue(
        text="DRAFT",
        description="""No PENDING annotations, but may have validation warnings - review is complete but needs refinement""")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="No PENDING annotations and no validation warnings - review is fully complete and validated")

    _defn = EnumDefinition(
        name="GeneReviewStatusEnum",
        description="Status of the gene review process",
    )

class ManuscriptSection(EnumDefinitionImpl):
    """
    Sections of a scientific manuscript or publication
    """
    TITLE = PermissibleValue(
        text="TITLE",
        description="Title section",
        meaning=IAO["0000305"])
    ABSTRACT = PermissibleValue(
        text="ABSTRACT",
        description="Abstract",
        meaning=IAO["0000315"])
    KEYWORDS = PermissibleValue(
        text="KEYWORDS",
        description="Keywords",
        meaning=IAO["0000630"])
    INTRODUCTION = PermissibleValue(
        text="INTRODUCTION",
        description="Introduction/Background",
        meaning=IAO["0000316"])
    LITERATURE_REVIEW = PermissibleValue(
        text="LITERATURE_REVIEW",
        description="Literature review",
        meaning=IAO["0000639"])
    METHODS = PermissibleValue(
        text="METHODS",
        description="Methods/Materials and Methods",
        meaning=IAO["0000317"])
    RESULTS = PermissibleValue(
        text="RESULTS",
        description="Results",
        meaning=IAO["0000318"])
    DISCUSSION = PermissibleValue(
        text="DISCUSSION",
        description="Discussion",
        meaning=IAO["0000319"])
    CONCLUSIONS = PermissibleValue(
        text="CONCLUSIONS",
        description="Conclusions",
        meaning=IAO["0000615"])
    APPENDICES = PermissibleValue(
        text="APPENDICES",
        description="Appendices",
        meaning=IAO["0000326"])
    SUPPLEMENTARY_MATERIAL = PermissibleValue(
        text="SUPPLEMENTARY_MATERIAL",
        description="Supplementary material",
        meaning=IAO["0000326"])
    DATABASE_ENTRY = PermissibleValue(
        text="DATABASE_ENTRY",
        description="Database entry")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other main text section")

    _defn = EnumDefinition(
        name="ManuscriptSection",
        description="Sections of a scientific manuscript or publication",
    )

class RuleTypeEnum(EnumDefinitionImpl):
    """
    Type of UniProt annotation rule
    """
    ARBA = PermissibleValue(
        text="ARBA",
        description="Association-Rule-Based Annotator rule (automatically mined)")
    UNIRULE = PermissibleValue(
        text="UNIRULE",
        description="Expert-curated UniRule")

    _defn = EnumDefinition(
        name="RuleTypeEnum",
        description="Type of UniProt annotation rule",
    )

class RuleReviewStatusEnum(EnumDefinitionImpl):
    """
    Status of the rule review
    """
    PENDING = PermissibleValue(
        text="PENDING",
        description="Review has not been started")
    IN_PROGRESS = PermissibleValue(
        text="IN_PROGRESS",
        description="Review is underway")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="Review is complete")

    _defn = EnumDefinition(
        name="RuleReviewStatusEnum",
        description="Status of the rule review",
    )

class RuleActionEnum(EnumDefinitionImpl):
    """
    Recommended action for the rule
    """
    ACCEPT = PermissibleValue(
        text="ACCEPT",
        description="Rule is correct and should be kept as-is")
    MODIFY = PermissibleValue(
        text="MODIFY",
        description="Rule needs modification (see suggested_modifications)")
    DEPRECATE = PermissibleValue(
        text="DEPRECATE",
        description="Rule should be removed or retired")
    SPLIT = PermissibleValue(
        text="SPLIT",
        description="Rule should be split into multiple more specific rules")
    MERGE = PermissibleValue(
        text="MERGE",
        description="Rule should be merged with another related rule")
    UNDECIDED = PermissibleValue(
        text="UNDECIDED",
        description="Unable to determine appropriate action")

    _defn = EnumDefinition(
        name="RuleActionEnum",
        description="Recommended action for the rule",
    )

class ParsimonyEnum(EnumDefinitionImpl):
    """
    Assessment of rule parsimony (simplicity vs complexity)
    """
    PARSIMONIOUS = PermissibleValue(
        text="PARSIMONIOUS",
        description="Rule is appropriately simple - conditions are necessary and sufficient")
    ACCEPTABLE = PermissibleValue(
        text="ACCEPTABLE",
        description="Rule complexity is reasonable given the biological context")
    REDUNDANT = PermissibleValue(
        text="REDUNDANT",
        description="Some conditions are redundant and could be removed")
    OVERLY_COMPLEX = PermissibleValue(
        text="OVERLY_COMPLEX",
        description="Rule has unnecessary complexity that should be simplified")

    _defn = EnumDefinition(
        name="ParsimonyEnum",
        description="Assessment of rule parsimony (simplicity vs complexity)",
    )

class LiteratureSupportEnum(EnumDefinitionImpl):
    """
    Level of literature support for the rule
    """
    STRONG = PermissibleValue(
        text="STRONG",
        description="Multiple high-quality papers directly support the domain-function relationship")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Some supporting evidence exists but not comprehensive")
    WEAK = PermissibleValue(
        text="WEAK",
        description="Limited evidence, mostly indirect or from computational studies")
    NONE = PermissibleValue(
        text="NONE",
        description="No literature support found")
    CONTRADICTED = PermissibleValue(
        text="CONTRADICTED",
        description="Literature contradicts the rule's predicted function")

    _defn = EnumDefinition(
        name="LiteratureSupportEnum",
        description="Level of literature support for the rule",
    )

class OverlapEnum(EnumDefinitionImpl):
    """
    Assessment of condition overlap/redundancy
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Conditions are independent and non-overlapping")
    MINOR = PermissibleValue(
        text="MINOR",
        description="Slight overlap but conditions add meaningful specificity")
    SIGNIFICANT = PermissibleValue(
        text="SIGNIFICANT",
        description="Substantial overlap - conditions may be capturing the same thing")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="Conditions are essentially equivalent/redundant")

    _defn = EnumDefinition(
        name="OverlapEnum",
        description="Assessment of condition overlap/redundancy",
    )

class SpecificityEnum(EnumDefinitionImpl):
    """
    Assessment of GO term specificity
    """
    TOO_BROAD = PermissibleValue(
        text="TOO_BROAD",
        description="GO term is too general - a more specific term should be used")
    APPROPRIATE = PermissibleValue(
        text="APPROPRIATE",
        description="GO term specificity matches the evidence")
    TOO_NARROW = PermissibleValue(
        text="TOO_NARROW",
        description="GO term is overly specific for what the domains predict")
    MISMATCHED = PermissibleValue(
        text="MISMATCHED",
        description="GO term is in wrong branch or aspect")

    _defn = EnumDefinition(
        name="SpecificityEnum",
        description="Assessment of GO term specificity",
    )

class TaxonomicScopeEnum(EnumDefinitionImpl):
    """
    Assessment of taxonomic restriction appropriateness
    """
    TOO_BROAD = PermissibleValue(
        text="TOO_BROAD",
        description="Taxon is too inclusive - should be restricted further")
    APPROPRIATE = PermissibleValue(
        text="APPROPRIATE",
        description="Taxonomic scope matches the domain's evolutionary distribution")
    TOO_NARROW = PermissibleValue(
        text="TOO_NARROW",
        description="Taxon is overly restrictive - function applies more broadly")
    MISSING = PermissibleValue(
        text="MISSING",
        description="Rule lacks necessary taxonomic restriction")
    UNNECESSARY = PermissibleValue(
        text="UNNECESSARY",
        description="Taxonomic restriction is not needed for this domain")

    _defn = EnumDefinition(
        name="TaxonomicScopeEnum",
        description="Assessment of taxonomic restriction appropriateness",
    )

class ConditionTypeEnum(EnumDefinitionImpl):
    """
    Types of conditions in rule antecedents
    """
    INTERPRO = PermissibleValue(
        text="INTERPRO",
        description="InterPro domain/family")
    FUNFAM = PermissibleValue(
        text="FUNFAM",
        description="CATH FunFam functional family")
    PANTHER = PermissibleValue(
        text="PANTHER",
        description="PANTHER family")
    PFAM = PermissibleValue(
        text="PFAM",
        description="Pfam domain")
    TAXON = PermissibleValue(
        text="TAXON",
        description="Taxonomic constraint")
    SEQUENCE_LENGTH = PermissibleValue(
        text="SEQUENCE_LENGTH",
        description="Sequence length constraint")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Other condition type")

    _defn = EnumDefinition(
        name="ConditionTypeEnum",
        description="Types of conditions in rule antecedents",
    )

class ProteinDatabaseEnum(EnumDefinitionImpl):
    """
    Protein database types for rule analysis
    """
    SWISSPROT = PermissibleValue(
        text="SWISSPROT",
        description="Swiss-Prot (reviewed, manually curated proteins)")
    TREMBL = PermissibleValue(
        text="TREMBL",
        description="TrEMBL (unreviewed, automatically annotated proteins)")
    UNIPROT = PermissibleValue(
        text="UNIPROT",
        description="Full UniProtKB (Swiss-Prot + TrEMBL)")

    _defn = EnumDefinition(
        name="ProteinDatabaseEnum",
        description="Protein database types for rule analysis",
    )

class InterProTypeEnum(EnumDefinitionImpl):
    """
    InterPro entry types categorizing protein signatures
    """
    FAMILY = PermissibleValue(
        text="FAMILY",
        description="Protein family (groups of proteins sharing similar sequence and function)")
    DOMAIN = PermissibleValue(
        text="DOMAIN",
        description="Protein domain (distinct functional or structural unit)")
    ACTIVE_SITE = PermissibleValue(
        text="ACTIVE_SITE",
        description="Active site (residues directly involved in catalysis)")
    BINDING_SITE = PermissibleValue(
        text="BINDING_SITE",
        description="Binding site (residues involved in binding substrates/ligands)")
    CONSERVED_SITE = PermissibleValue(
        text="CONSERVED_SITE",
        description="Conserved site (conserved residues with functional significance)")
    REPEAT = PermissibleValue(
        text="REPEAT",
        description="Repeat (short sequence motif that occurs multiple times)")
    HOMOLOGOUS_SUPERFAMILY = PermissibleValue(
        text="HOMOLOGOUS_SUPERFAMILY",
        description="Homologous superfamily (proteins with distant evolutionary relationships)")
    PTM = PermissibleValue(
        text="PTM",
        description="Post-translational modification site")

    _defn = EnumDefinition(
        name="InterProTypeEnum",
        description="InterPro entry types categorizing protein signatures",
    )

class OverlapInterpretationEnum(EnumDefinitionImpl):
    """
    Automated interpretation of domain overlap patterns
    """
    REDUNDANT = PermissibleValue(
        text="REDUNDANT",
        description="Very high overlap (Jaccard > 0.9), conditions are nearly identical")
    SUBSET = PermissibleValue(
        text="SUBSET",
        description="One condition is a subset of the other (containment > 0.95)")
    HIGH_OVERLAP = PermissibleValue(
        text="HIGH_OVERLAP",
        description="High overlap (Jaccard > 0.5), conditions are similar")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Moderate overlap (0.2 < Jaccard <= 0.5)")
    LOW = PermissibleValue(
        text="LOW",
        description="Low overlap (Jaccard <= 0.2), conditions are mostly distinct")
    DISJOINT = PermissibleValue(
        text="DISJOINT",
        description="No overlap (intersection = 0), conditions are completely distinct")

    _defn = EnumDefinition(
        name="OverlapInterpretationEnum",
        description="Automated interpretation of domain overlap patterns",
    )

class EntryTypeEnum(EnumDefinitionImpl):
    """
    Type of entry in a rule review (domain/family condition or GO term target)
    """
    INTERPRO = PermissibleValue(
        text="INTERPRO",
        description="InterPro entry (domain, family, repeat, etc.)")
    FUNFAM = PermissibleValue(
        text="FUNFAM",
        description="CATH FunFam (functional family from CATH database)")
    PANTHER = PermissibleValue(
        text="PANTHER",
        description="PANTHER family or subfamily")
    GO_TERM = PermissibleValue(
        text="GO_TERM",
        description="Gene Ontology term (annotation target)")

    _defn = EnumDefinition(
        name="EntryTypeEnum",
        description="Type of entry in a rule review (domain/family condition or GO term target)",
    )

class EntryRelationshipEnum(EnumDefinitionImpl):
    """
    Type of relationship between entries in a rule
    """
    PREDICTS = PermissibleValue(
        text="PREDICTS",
        description="""This entry predicts the target (this ⊆ target). Selected when containment_a_in_b is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.""")
    PREDICTED_BY = PermissibleValue(
        text="PREDICTED_BY",
        description="""This entry is predicted by the target (target ⊆ this). Selected when containment_b_in_a is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.""")
    EQUIV = PermissibleValue(
        text="EQUIV",
        description="""This entry is equivalent to the target (bidirectional high similarity). Selected when jaccard_boosted (jaccard + 0.05) is highest among {jaccard+0.05, containment_a_in_b, containment_b_in_a}.""")

    _defn = EnumDefinition(
        name="EntryRelationshipEnum",
        description="Type of relationship between entries in a rule",
    )

class FunctionalIsoformTypeEnum(EnumDefinitionImpl):
    """
    Type of functional isoform or product. Distinguishes between different mechanisms that produce functionally
    distinct forms of a gene product.
    """
    SPLICE_VARIANT = PermissibleValue(
        text="SPLICE_VARIANT",
        description="""Alternative splicing produces functionally distinct isoforms. Maps to one or more UniProt isoform IDs (e.g., P19544-1, P19544-2).""")
    SPLICE_CLASS = PermissibleValue(
        text="SPLICE_CLASS",
        description="""A class of splice variants that share functional properties. Groups multiple UniProt isoform IDs that have similar functions. Example: WT1 +KTS isoforms (multiple UniProt IDs) vs -KTS isoforms.""")
    CLEAVAGE_PRODUCT = PermissibleValue(
        text="CLEAVAGE_PRODUCT",
        description="""Post-translational proteolytic cleavage produces distinct peptides. Maps to UniProt chain IDs (PRO_NNNNNNN from FT PEPTIDE lines). Example: POMC cleavage into ACTH, alpha-MSH, beta-endorphin.""")
    MODIFICATION_STATE = PermissibleValue(
        text="MODIFICATION_STATE",
        description="""Post-translational modification creates functionally distinct forms. Example: Phosphorylated vs unphosphorylated forms with different activities.""")
    CONFORMATIONAL_STATE = PermissibleValue(
        text="CONFORMATIONAL_STATE",
        description="""Different conformational states with distinct functions. Example: GTP-bound vs GDP-bound forms of GTPases.""")

    _defn = EnumDefinition(
        name="FunctionalIsoformTypeEnum",
        description="""Type of functional isoform or product. Distinguishes between different mechanisms that produce functionally distinct forms of a gene product.""",
    )

class FunctionalIsoformMappingTypeEnum(EnumDefinitionImpl):
    """
    Type of identifier that a functional isoform maps to
    """
    UNIPROT_ISOFORM = PermissibleValue(
        text="UNIPROT_ISOFORM",
        description="UniProt isoform ID (e.g., P19544-1, Q07817-2)")
    UNIPROT_CHAIN = PermissibleValue(
        text="UNIPROT_CHAIN",
        description="UniProt chain/peptide ID from FT PEPTIDE (e.g., PRO_0000024969)")

    _defn = EnumDefinition(
        name="FunctionalIsoformMappingTypeEnum",
        description="Type of identifier that a functional isoform maps to",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=GENE_REVIEW.id, name="id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.id, domain=None, range=URIRef)

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=GENE_REVIEW.label, domain=None, range=str)

slots.gene_symbol = Slot(uri=GENE_REVIEW.gene_symbol, name="gene_symbol", curie=GENE_REVIEW.curie('gene_symbol'),
                   model_uri=GENE_REVIEW.gene_symbol, domain=None, range=str)

slots.product_type = Slot(uri=GENE_REVIEW.product_type, name="product_type", curie=GENE_REVIEW.curie('product_type'),
                   model_uri=GENE_REVIEW.product_type, domain=None, range=Optional[Union[str, "ProductTypeEnum"]])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=GENE_REVIEW.title, domain=None, range=str)

slots.aliases = Slot(uri=GENE_REVIEW.aliases, name="aliases", curie=GENE_REVIEW.curie('aliases'),
                   model_uri=GENE_REVIEW.aliases, domain=None, range=Optional[Union[str, list[str]]])

slots.name = Slot(uri=GENE_REVIEW.name, name="name", curie=GENE_REVIEW.curie('name'),
                   model_uri=GENE_REVIEW.name, domain=None, range=Optional[str])

slots.sequence_note = Slot(uri=GENE_REVIEW.sequence_note, name="sequence_note", curie=GENE_REVIEW.curie('sequence_note'),
                   model_uri=GENE_REVIEW.sequence_note, domain=None, range=Optional[str])

slots.tags = Slot(uri=GENE_REVIEW.tags, name="tags", curie=GENE_REVIEW.curie('tags'),
                   model_uri=GENE_REVIEW.tags, domain=None, range=Optional[Union[str, list[str]]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.description, domain=None, range=Optional[str])

slots.statement = Slot(uri=GENE_REVIEW.statement, name="statement", curie=GENE_REVIEW.curie('statement'),
                   model_uri=GENE_REVIEW.statement, domain=None, range=Optional[str])

slots.references = Slot(uri=GENE_REVIEW.references, name="references", curie=GENE_REVIEW.curie('references'),
                   model_uri=GENE_REVIEW.references, domain=None, range=Optional[Union[dict[Union[str, ReferenceId], Union[dict, Reference]], list[Union[dict, Reference]]]])

slots.findings = Slot(uri=GENE_REVIEW.findings, name="findings", curie=GENE_REVIEW.curie('findings'),
                   model_uri=GENE_REVIEW.findings, domain=None, range=Optional[Union[Union[dict, Finding], list[Union[dict, Finding]]]])

slots.supported_by = Slot(uri=GENE_REVIEW.supported_by, name="supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.summary = Slot(uri=GENE_REVIEW.summary, name="summary", curie=GENE_REVIEW.curie('summary'),
                   model_uri=GENE_REVIEW.summary, domain=None, range=Optional[str])

slots.supporting_text = Slot(uri=GENE_REVIEW.supporting_text, name="supporting_text", curie=GENE_REVIEW.curie('supporting_text'),
                   model_uri=GENE_REVIEW.supporting_text, domain=None, range=Optional[str])

slots.supporting_text_fulltext = Slot(uri=GENE_REVIEW.supporting_text_fulltext, name="supporting_text_fulltext", curie=GENE_REVIEW.curie('supporting_text_fulltext'),
                   model_uri=GENE_REVIEW.supporting_text_fulltext, domain=None, range=Optional[str])

slots.full_text_unavailable = Slot(uri=GENE_REVIEW.full_text_unavailable, name="full_text_unavailable", curie=GENE_REVIEW.curie('full_text_unavailable'),
                   model_uri=GENE_REVIEW.full_text_unavailable, domain=None, range=Optional[Union[bool, Bool]])

slots.evidence_type = Slot(uri=GENE_REVIEW.evidence_type, name="evidence_type", curie=GENE_REVIEW.curie('evidence_type'),
                   model_uri=GENE_REVIEW.evidence_type, domain=None, range=Union[str, "EvidenceType"])

slots.term = Slot(uri=GENE_REVIEW.term, name="term", curie=GENE_REVIEW.curie('term'),
                   model_uri=GENE_REVIEW.term, domain=None, range=Optional[Union[dict, Term]])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=GENE_REVIEW.predicate, domain=None, range=str)

slots.taxon = Slot(uri=GENE_REVIEW.taxon, name="taxon", curie=GENE_REVIEW.curie('taxon'),
                   model_uri=GENE_REVIEW.taxon, domain=None, range=Union[dict, Term])

slots.alternative_products = Slot(uri=GENE_REVIEW.alternative_products, name="alternative_products", curie=GENE_REVIEW.curie('alternative_products'),
                   model_uri=GENE_REVIEW.alternative_products, domain=None, range=Optional[Union[dict[Union[str, AlternativeProductId], Union[dict, AlternativeProduct]], list[Union[dict, AlternativeProduct]]]])

slots.functional_isoforms = Slot(uri=GENE_REVIEW.functional_isoforms, name="functional_isoforms", curie=GENE_REVIEW.curie('functional_isoforms'),
                   model_uri=GENE_REVIEW.functional_isoforms, domain=None, range=Optional[Union[dict[Union[str, FunctionalIsoformId], Union[dict, FunctionalIsoform]], list[Union[dict, FunctionalIsoform]]]])

slots.existing_annotations = Slot(uri=GENE_REVIEW.existing_annotations, name="existing_annotations", curie=GENE_REVIEW.curie('existing_annotations'),
                   model_uri=GENE_REVIEW.existing_annotations, domain=None, range=Optional[Union[Union[dict, ExistingAnnotation], list[Union[dict, ExistingAnnotation]]]])

slots.core_functions = Slot(uri=GENE_REVIEW.core_functions, name="core_functions", curie=GENE_REVIEW.curie('core_functions'),
                   model_uri=GENE_REVIEW.core_functions, domain=None, range=Optional[Union[Union[dict, CoreFunction], list[Union[dict, CoreFunction]]]])

slots.action = Slot(uri=GENE_REVIEW.action, name="action", curie=GENE_REVIEW.curie('action'),
                   model_uri=GENE_REVIEW.action, domain=None, range=Union[str, "ActionEnum"])

slots.reason = Slot(uri=GENE_REVIEW.reason, name="reason", curie=GENE_REVIEW.curie('reason'),
                   model_uri=GENE_REVIEW.reason, domain=None, range=Optional[str])

slots.proposed_replacement_terms = Slot(uri=GENE_REVIEW.proposed_replacement_terms, name="proposed_replacement_terms", curie=GENE_REVIEW.curie('proposed_replacement_terms'),
                   model_uri=GENE_REVIEW.proposed_replacement_terms, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.extensions = Slot(uri=GENE_REVIEW.extensions, name="extensions", curie=GENE_REVIEW.curie('extensions'),
                   model_uri=GENE_REVIEW.extensions, domain=None, range=Optional[Union[Union[dict, AnnotationExtension], list[Union[dict, AnnotationExtension]]]])

slots.negated = Slot(uri=GENE_REVIEW.negated, name="negated", curie=GENE_REVIEW.curie('negated'),
                   model_uri=GENE_REVIEW.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.reference_id = Slot(uri=GENE_REVIEW.reference_id, name="reference_id", curie=GENE_REVIEW.curie('reference_id'),
                   model_uri=GENE_REVIEW.reference_id, domain=None, range=Union[str, ReferenceId])

slots.original_reference_id = Slot(uri=GENE_REVIEW.original_reference_id, name="original_reference_id", curie=GENE_REVIEW.curie('original_reference_id'),
                   model_uri=GENE_REVIEW.original_reference_id, domain=None, range=Optional[Union[str, ReferenceId]])

slots.retired = Slot(uri=GENE_REVIEW.retired, name="retired", curie=GENE_REVIEW.curie('retired'),
                   model_uri=GENE_REVIEW.retired, domain=None, range=Optional[Union[bool, Bool]])

slots.isoform = Slot(uri=GENE_REVIEW.isoform, name="isoform", curie=GENE_REVIEW.curie('isoform'),
                   model_uri=GENE_REVIEW.isoform, domain=None, range=Optional[str])

slots.review = Slot(uri=GENE_REVIEW.review, name="review", curie=GENE_REVIEW.curie('review'),
                   model_uri=GENE_REVIEW.review, domain=None, range=Optional[Union[dict, Review]])

slots.ontology = Slot(uri=GENE_REVIEW.ontology, name="ontology", curie=GENE_REVIEW.curie('ontology'),
                   model_uri=GENE_REVIEW.ontology, domain=None, range=Optional[str])

slots.supporting_entities = Slot(uri=GENE_REVIEW.supporting_entities, name="supporting_entities", curie=GENE_REVIEW.curie('supporting_entities'),
                   model_uri=GENE_REVIEW.supporting_entities, domain=None, range=Optional[Union[str, list[str]]])

slots.additional_reference_ids = Slot(uri=GENE_REVIEW.additional_reference_ids, name="additional_reference_ids", curie=GENE_REVIEW.curie('additional_reference_ids'),
                   model_uri=GENE_REVIEW.additional_reference_ids, domain=None, range=Optional[Union[Union[str, ReferenceId], list[Union[str, ReferenceId]]]])

slots.is_invalid = Slot(uri=GENE_REVIEW.is_invalid, name="is_invalid", curie=GENE_REVIEW.curie('is_invalid'),
                   model_uri=GENE_REVIEW.is_invalid, domain=None, range=Optional[Union[bool, Bool]])

slots.reference_section_type = Slot(uri=GENE_REVIEW.reference_section_type, name="reference_section_type", curie=GENE_REVIEW.curie('reference_section_type'),
                   model_uri=GENE_REVIEW.reference_section_type, domain=None, range=Optional[Union[str, "ManuscriptSection"]])

slots.proposed_new_terms = Slot(uri=GENE_REVIEW.proposed_new_terms, name="proposed_new_terms", curie=GENE_REVIEW.curie('proposed_new_terms'),
                   model_uri=GENE_REVIEW.proposed_new_terms, domain=None, range=Optional[Union[Union[dict, ProposedOntologyTerm], list[Union[dict, ProposedOntologyTerm]]]])

slots.suggested_questions = Slot(uri=GENE_REVIEW.suggested_questions, name="suggested_questions", curie=GENE_REVIEW.curie('suggested_questions'),
                   model_uri=GENE_REVIEW.suggested_questions, domain=None, range=Optional[Union[Union[dict, Question], list[Union[dict, Question]]]])

slots.suggested_experiments = Slot(uri=GENE_REVIEW.suggested_experiments, name="suggested_experiments", curie=GENE_REVIEW.curie('suggested_experiments'),
                   model_uri=GENE_REVIEW.suggested_experiments, domain=None, range=Optional[Union[Union[dict, Experiment], list[Union[dict, Experiment]]]])

slots.status = Slot(uri=GENE_REVIEW.status, name="status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.status, domain=None, range=Optional[Union[str, "GeneReviewStatusEnum"]])

slots.functionalIsoform__id = Slot(uri=GENE_REVIEW.id, name="functionalIsoform__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.functionalIsoform__id, domain=None, range=URIRef)

slots.functionalIsoform__name = Slot(uri=GENE_REVIEW.name, name="functionalIsoform__name", curie=GENE_REVIEW.curie('name'),
                   model_uri=GENE_REVIEW.functionalIsoform__name, domain=None, range=str)

slots.functionalIsoform__type = Slot(uri=GENE_REVIEW.type, name="functionalIsoform__type", curie=GENE_REVIEW.curie('type'),
                   model_uri=GENE_REVIEW.functionalIsoform__type, domain=None, range=Union[str, "FunctionalIsoformTypeEnum"])

slots.functionalIsoform__maps_to = Slot(uri=GENE_REVIEW.maps_to, name="functionalIsoform__maps_to", curie=GENE_REVIEW.curie('maps_to'),
                   model_uri=GENE_REVIEW.functionalIsoform__maps_to, domain=None, range=Optional[Union[Union[dict, FunctionalIsoformMapping], list[Union[dict, FunctionalIsoformMapping]]]])

slots.functionalIsoform__description = Slot(uri=GENE_REVIEW.description, name="functionalIsoform__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.functionalIsoform__description, domain=None, range=str)

slots.functionalIsoform__isoform_specific_terms = Slot(uri=GENE_REVIEW.isoform_specific_terms, name="functionalIsoform__isoform_specific_terms", curie=GENE_REVIEW.curie('isoform_specific_terms'),
                   model_uri=GENE_REVIEW.functionalIsoform__isoform_specific_terms, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.functionalIsoformMapping__type = Slot(uri=GENE_REVIEW.type, name="functionalIsoformMapping__type", curie=GENE_REVIEW.curie('type'),
                   model_uri=GENE_REVIEW.functionalIsoformMapping__type, domain=None, range=Union[str, "FunctionalIsoformMappingTypeEnum"])

slots.functionalIsoformMapping__ids = Slot(uri=GENE_REVIEW.ids, name="functionalIsoformMapping__ids", curie=GENE_REVIEW.curie('ids'),
                   model_uri=GENE_REVIEW.functionalIsoformMapping__ids, domain=None, range=Union[str, list[str]])

slots.functionalIsoformMapping__residues = Slot(uri=GENE_REVIEW.residues, name="functionalIsoformMapping__residues", curie=GENE_REVIEW.curie('residues'),
                   model_uri=GENE_REVIEW.functionalIsoformMapping__residues, domain=None, range=Optional[str])

slots.coreFunction__description = Slot(uri=GENE_REVIEW.description, name="coreFunction__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.coreFunction__description, domain=None, range=Optional[str])

slots.coreFunction__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="coreFunction__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.coreFunction__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.coreFunction__molecular_function = Slot(uri=GENE_REVIEW.molecular_function, name="coreFunction__molecular_function", curie=GENE_REVIEW.curie('molecular_function'),
                   model_uri=GENE_REVIEW.coreFunction__molecular_function, domain=None, range=Union[dict, Term])

slots.coreFunction__directly_involved_in = Slot(uri=GENE_REVIEW.directly_involved_in, name="coreFunction__directly_involved_in", curie=GENE_REVIEW.curie('directly_involved_in'),
                   model_uri=GENE_REVIEW.coreFunction__directly_involved_in, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__locations = Slot(uri=GENE_REVIEW.locations, name="coreFunction__locations", curie=GENE_REVIEW.curie('locations'),
                   model_uri=GENE_REVIEW.coreFunction__locations, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__anatomical_locations = Slot(uri=GENE_REVIEW.anatomical_locations, name="coreFunction__anatomical_locations", curie=GENE_REVIEW.curie('anatomical_locations'),
                   model_uri=GENE_REVIEW.coreFunction__anatomical_locations, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__substrates = Slot(uri=GENE_REVIEW.substrates, name="coreFunction__substrates", curie=GENE_REVIEW.curie('substrates'),
                   model_uri=GENE_REVIEW.coreFunction__substrates, domain=None, range=Optional[Union[dict[Union[str, TermId], Union[dict, Term]], list[Union[dict, Term]]]])

slots.coreFunction__in_complex = Slot(uri=GENE_REVIEW.in_complex, name="coreFunction__in_complex", curie=GENE_REVIEW.curie('in_complex'),
                   model_uri=GENE_REVIEW.coreFunction__in_complex, domain=None, range=Optional[Union[dict, Term]])

slots.termMapping__predicate = Slot(uri=GENE_REVIEW.predicate, name="termMapping__predicate", curie=GENE_REVIEW.curie('predicate'),
                   model_uri=GENE_REVIEW.termMapping__predicate, domain=None, range=str)

slots.termMapping__target_term = Slot(uri=GENE_REVIEW.target_term, name="termMapping__target_term", curie=GENE_REVIEW.curie('target_term'),
                   model_uri=GENE_REVIEW.termMapping__target_term, domain=None, range=Union[dict, Term])

slots.proposedOntologyTerm__proposed_name = Slot(uri=GENE_REVIEW.proposed_name, name="proposedOntologyTerm__proposed_name", curie=GENE_REVIEW.curie('proposed_name'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_name, domain=None, range=str)

slots.proposedOntologyTerm__proposed_definition = Slot(uri=GENE_REVIEW.proposed_definition, name="proposedOntologyTerm__proposed_definition", curie=GENE_REVIEW.curie('proposed_definition'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_definition, domain=None, range=str)

slots.proposedOntologyTerm__justification = Slot(uri=GENE_REVIEW.justification, name="proposedOntologyTerm__justification", curie=GENE_REVIEW.curie('justification'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__justification, domain=None, range=Optional[str])

slots.proposedOntologyTerm__proposed_parent = Slot(uri=GENE_REVIEW.proposed_parent, name="proposedOntologyTerm__proposed_parent", curie=GENE_REVIEW.curie('proposed_parent'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_parent, domain=None, range=Optional[Union[dict, Term]])

slots.proposedOntologyTerm__proposed_mappings = Slot(uri=GENE_REVIEW.proposed_mappings, name="proposedOntologyTerm__proposed_mappings", curie=GENE_REVIEW.curie('proposed_mappings'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__proposed_mappings, domain=None, range=Optional[Union[Union[dict, TermMapping], list[Union[dict, TermMapping]]]])

slots.proposedOntologyTerm__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="proposedOntologyTerm__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.proposedOntologyTerm__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.experiment__hypothesis = Slot(uri=GENE_REVIEW.hypothesis, name="experiment__hypothesis", curie=GENE_REVIEW.curie('hypothesis'),
                   model_uri=GENE_REVIEW.experiment__hypothesis, domain=None, range=Optional[str])

slots.experiment__description = Slot(uri=GENE_REVIEW.description, name="experiment__description", curie=GENE_REVIEW.curie('description'),
                   model_uri=GENE_REVIEW.experiment__description, domain=None, range=str)

slots.experiment__experiment_type = Slot(uri=GENE_REVIEW.experiment_type, name="experiment__experiment_type", curie=GENE_REVIEW.curie('experiment_type'),
                   model_uri=GENE_REVIEW.experiment__experiment_type, domain=None, range=Optional[str])

slots.question__question = Slot(uri=GENE_REVIEW.question, name="question__question", curie=GENE_REVIEW.curie('question'),
                   model_uri=GENE_REVIEW.question__question, domain=None, range=str)

slots.question__experts = Slot(uri=GENE_REVIEW.experts, name="question__experts", curie=GENE_REVIEW.curie('experts'),
                   model_uri=GENE_REVIEW.question__experts, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleReview__status = Slot(uri=GENE_REVIEW.status, name="ruleReview__status", curie=GENE_REVIEW.curie('status'),
                   model_uri=GENE_REVIEW.ruleReview__status, domain=None, range=Optional[Union[str, "RuleReviewStatusEnum"]])

slots.ruleReview__rule_type = Slot(uri=GENE_REVIEW.rule_type, name="ruleReview__rule_type", curie=GENE_REVIEW.curie('rule_type'),
                   model_uri=GENE_REVIEW.ruleReview__rule_type, domain=None, range=Union[str, "RuleTypeEnum"])

slots.ruleReview__rule = Slot(uri=GENE_REVIEW.rule, name="ruleReview__rule", curie=GENE_REVIEW.curie('rule'),
                   model_uri=GENE_REVIEW.ruleReview__rule, domain=None, range=Union[dict, EmbeddedRule])

slots.ruleReview__review_summary = Slot(uri=GENE_REVIEW.review_summary, name="ruleReview__review_summary", curie=GENE_REVIEW.curie('review_summary'),
                   model_uri=GENE_REVIEW.ruleReview__review_summary, domain=None, range=Optional[str])

slots.ruleReview__action = Slot(uri=GENE_REVIEW.action, name="ruleReview__action", curie=GENE_REVIEW.curie('action'),
                   model_uri=GENE_REVIEW.ruleReview__action, domain=None, range=Union[str, "RuleActionEnum"])

slots.ruleReview__action_rationale = Slot(uri=GENE_REVIEW.action_rationale, name="ruleReview__action_rationale", curie=GENE_REVIEW.curie('action_rationale'),
                   model_uri=GENE_REVIEW.ruleReview__action_rationale, domain=None, range=Optional[str])

slots.ruleReview__suggested_modifications = Slot(uri=GENE_REVIEW.suggested_modifications, name="ruleReview__suggested_modifications", curie=GENE_REVIEW.curie('suggested_modifications'),
                   model_uri=GENE_REVIEW.ruleReview__suggested_modifications, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleReview__parsimony = Slot(uri=GENE_REVIEW.parsimony, name="ruleReview__parsimony", curie=GENE_REVIEW.curie('parsimony'),
                   model_uri=GENE_REVIEW.ruleReview__parsimony, domain=None, range=Optional[Union[dict, ParsimonyAssessment]])

slots.ruleReview__literature_support = Slot(uri=GENE_REVIEW.literature_support, name="ruleReview__literature_support", curie=GENE_REVIEW.curie('literature_support'),
                   model_uri=GENE_REVIEW.ruleReview__literature_support, domain=None, range=Optional[Union[dict, LiteratureSupportAssessment]])

slots.ruleReview__condition_overlap = Slot(uri=GENE_REVIEW.condition_overlap, name="ruleReview__condition_overlap", curie=GENE_REVIEW.curie('condition_overlap'),
                   model_uri=GENE_REVIEW.ruleReview__condition_overlap, domain=None, range=Optional[Union[dict, ConditionOverlapAssessment]])

slots.ruleReview__go_specificity = Slot(uri=GENE_REVIEW.go_specificity, name="ruleReview__go_specificity", curie=GENE_REVIEW.curie('go_specificity'),
                   model_uri=GENE_REVIEW.ruleReview__go_specificity, domain=None, range=Optional[Union[dict, GOSpecificityAssessment]])

slots.ruleReview__taxonomic_scope = Slot(uri=GENE_REVIEW.taxonomic_scope, name="ruleReview__taxonomic_scope", curie=GENE_REVIEW.curie('taxonomic_scope'),
                   model_uri=GENE_REVIEW.ruleReview__taxonomic_scope, domain=None, range=Optional[Union[dict, TaxonomicScopeAssessment]])

slots.ruleReview__confidence = Slot(uri=GENE_REVIEW.confidence, name="ruleReview__confidence", curie=GENE_REVIEW.curie('confidence'),
                   model_uri=GENE_REVIEW.ruleReview__confidence, domain=None, range=Optional[float])

slots.ruleReview__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="ruleReview__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.ruleReview__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.embeddedRule__rule_id = Slot(uri=GENE_REVIEW.rule_id, name="embeddedRule__rule_id", curie=GENE_REVIEW.curie('rule_id'),
                   model_uri=GENE_REVIEW.embeddedRule__rule_id, domain=None, range=str)

slots.embeddedRule__condition_sets = Slot(uri=GENE_REVIEW.condition_sets, name="embeddedRule__condition_sets", curie=GENE_REVIEW.curie('condition_sets'),
                   model_uri=GENE_REVIEW.embeddedRule__condition_sets, domain=None, range=Union[Union[dict, RuleConditionSet], list[Union[dict, RuleConditionSet]]])

slots.embeddedRule__go_annotations = Slot(uri=GENE_REVIEW.go_annotations, name="embeddedRule__go_annotations", curie=GENE_REVIEW.curie('go_annotations'),
                   model_uri=GENE_REVIEW.embeddedRule__go_annotations, domain=None, range=Optional[Union[Union[dict, RuleGOAnnotation], list[Union[dict, RuleGOAnnotation]]]])

slots.embeddedRule__ipr2go_redundancy = Slot(uri=GENE_REVIEW.ipr2go_redundancy, name="embeddedRule__ipr2go_redundancy", curie=GENE_REVIEW.curie('ipr2go_redundancy'),
                   model_uri=GENE_REVIEW.embeddedRule__ipr2go_redundancy, domain=None, range=Optional[Union[dict, InterPro2GORedundancy]])

slots.embeddedRule__entries = Slot(uri=GENE_REVIEW.entries, name="embeddedRule__entries", curie=GENE_REVIEW.curie('entries'),
                   model_uri=GENE_REVIEW.embeddedRule__entries, domain=None, range=Union[dict[Union[str, RuleReviewEntryId], Union[dict, RuleReviewEntry]], list[Union[dict, RuleReviewEntry]]])

slots.embeddedRule__reviewed_protein_count = Slot(uri=GENE_REVIEW.reviewed_protein_count, name="embeddedRule__reviewed_protein_count", curie=GENE_REVIEW.curie('reviewed_protein_count'),
                   model_uri=GENE_REVIEW.embeddedRule__reviewed_protein_count, domain=None, range=Optional[int])

slots.embeddedRule__unreviewed_protein_count = Slot(uri=GENE_REVIEW.unreviewed_protein_count, name="embeddedRule__unreviewed_protein_count", curie=GENE_REVIEW.curie('unreviewed_protein_count'),
                   model_uri=GENE_REVIEW.embeddedRule__unreviewed_protein_count, domain=None, range=Optional[int])

slots.embeddedRule__created_date = Slot(uri=GENE_REVIEW.created_date, name="embeddedRule__created_date", curie=GENE_REVIEW.curie('created_date'),
                   model_uri=GENE_REVIEW.embeddedRule__created_date, domain=None, range=Optional[str])

slots.embeddedRule__modified_date = Slot(uri=GENE_REVIEW.modified_date, name="embeddedRule__modified_date", curie=GENE_REVIEW.curie('modified_date'),
                   model_uri=GENE_REVIEW.embeddedRule__modified_date, domain=None, range=Optional[str])

slots.ruleConditionSet__number = Slot(uri=GENE_REVIEW.number, name="ruleConditionSet__number", curie=GENE_REVIEW.curie('number'),
                   model_uri=GENE_REVIEW.ruleConditionSet__number, domain=None, range=int)

slots.ruleConditionSet__conditions = Slot(uri=GENE_REVIEW.conditions, name="ruleConditionSet__conditions", curie=GENE_REVIEW.curie('conditions'),
                   model_uri=GENE_REVIEW.ruleConditionSet__conditions, domain=None, range=Union[Union[dict, RuleCondition], list[Union[dict, RuleCondition]]])

slots.ruleConditionSet__notes = Slot(uri=GENE_REVIEW.notes, name="ruleConditionSet__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.ruleConditionSet__notes, domain=None, range=Optional[str])

slots.ruleConditionSet__pairwise_overlap = Slot(uri=GENE_REVIEW.pairwise_overlap, name="ruleConditionSet__pairwise_overlap", curie=GENE_REVIEW.curie('pairwise_overlap'),
                   model_uri=GENE_REVIEW.ruleConditionSet__pairwise_overlap, domain=None, range=Optional[Union[Union[dict, PairwiseOverlap], list[Union[dict, PairwiseOverlap]]]])

slots.ruleCondition__condition_type = Slot(uri=GENE_REVIEW.condition_type, name="ruleCondition__condition_type", curie=GENE_REVIEW.curie('condition_type'),
                   model_uri=GENE_REVIEW.ruleCondition__condition_type, domain=None, range=Union[str, "ConditionTypeEnum"])

slots.ruleCondition__value = Slot(uri=GENE_REVIEW.value, name="ruleCondition__value", curie=GENE_REVIEW.curie('value'),
                   model_uri=GENE_REVIEW.ruleCondition__value, domain=None, range=str)

slots.ruleCondition__curie = Slot(uri=GENE_REVIEW.curie, name="ruleCondition__curie", curie=GENE_REVIEW.curie('curie'),
                   model_uri=GENE_REVIEW.ruleCondition__curie, domain=None, range=Optional[str])

slots.ruleCondition__label = Slot(uri=GENE_REVIEW.label, name="ruleCondition__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.ruleCondition__label, domain=None, range=Optional[str])

slots.ruleCondition__interpro_type = Slot(uri=GENE_REVIEW.interpro_type, name="ruleCondition__interpro_type", curie=GENE_REVIEW.curie('interpro_type'),
                   model_uri=GENE_REVIEW.ruleCondition__interpro_type, domain=None, range=Optional[Union[str, "InterProTypeEnum"]])

slots.ruleCondition__negated = Slot(uri=GENE_REVIEW.negated, name="ruleCondition__negated", curie=GENE_REVIEW.curie('negated'),
                   model_uri=GENE_REVIEW.ruleCondition__negated, domain=None, range=Optional[Union[bool, Bool]])

slots.ruleCondition__protein_count = Slot(uri=GENE_REVIEW.protein_count, name="ruleCondition__protein_count", curie=GENE_REVIEW.curie('protein_count'),
                   model_uri=GENE_REVIEW.ruleCondition__protein_count, domain=None, range=Optional[int])

slots.ruleCondition__protein_database = Slot(uri=GENE_REVIEW.protein_database, name="ruleCondition__protein_database", curie=GENE_REVIEW.curie('protein_database'),
                   model_uri=GENE_REVIEW.ruleCondition__protein_database, domain=None, range=Optional[Union[str, "ProteinDatabaseEnum"]])

slots.ruleCondition__uniqueness_score = Slot(uri=GENE_REVIEW.uniqueness_score, name="ruleCondition__uniqueness_score", curie=GENE_REVIEW.curie('uniqueness_score'),
                   model_uri=GENE_REVIEW.ruleCondition__uniqueness_score, domain=None, range=Optional[float])

slots.ruleCondition__sample_proteins = Slot(uri=GENE_REVIEW.sample_proteins, name="ruleCondition__sample_proteins", curie=GENE_REVIEW.curie('sample_proteins'),
                   model_uri=GENE_REVIEW.ruleCondition__sample_proteins, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleGOAnnotation__go_id = Slot(uri=GENE_REVIEW.go_id, name="ruleGOAnnotation__go_id", curie=GENE_REVIEW.curie('go_id'),
                   model_uri=GENE_REVIEW.ruleGOAnnotation__go_id, domain=None, range=str)

slots.ruleGOAnnotation__go_label = Slot(uri=GENE_REVIEW.go_label, name="ruleGOAnnotation__go_label", curie=GENE_REVIEW.curie('go_label'),
                   model_uri=GENE_REVIEW.ruleGOAnnotation__go_label, domain=None, range=Optional[str])

slots.ruleGOAnnotation__aspect = Slot(uri=GENE_REVIEW.aspect, name="ruleGOAnnotation__aspect", curie=GENE_REVIEW.curie('aspect'),
                   model_uri=GENE_REVIEW.ruleGOAnnotation__aspect, domain=None, range=Optional[str])

slots.pairwiseOverlap__condition_a = Slot(uri=GENE_REVIEW.condition_a, name="pairwiseOverlap__condition_a", curie=GENE_REVIEW.curie('condition_a'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_a, domain=None, range=str)

slots.pairwiseOverlap__condition_b = Slot(uri=GENE_REVIEW.condition_b, name="pairwiseOverlap__condition_b", curie=GENE_REVIEW.curie('condition_b'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_b, domain=None, range=str)

slots.pairwiseOverlap__condition_a_label = Slot(uri=GENE_REVIEW.condition_a_label, name="pairwiseOverlap__condition_a_label", curie=GENE_REVIEW.curie('condition_a_label'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_a_label, domain=None, range=Optional[str])

slots.pairwiseOverlap__condition_b_label = Slot(uri=GENE_REVIEW.condition_b_label, name="pairwiseOverlap__condition_b_label", curie=GENE_REVIEW.curie('condition_b_label'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_b_label, domain=None, range=Optional[str])

slots.pairwiseOverlap__protein_database = Slot(uri=GENE_REVIEW.protein_database, name="pairwiseOverlap__protein_database", curie=GENE_REVIEW.curie('protein_database'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__protein_database, domain=None, range=Union[str, "ProteinDatabaseEnum"])

slots.pairwiseOverlap__count_a = Slot(uri=GENE_REVIEW.count_a, name="pairwiseOverlap__count_a", curie=GENE_REVIEW.curie('count_a'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__count_a, domain=None, range=int)

slots.pairwiseOverlap__count_b = Slot(uri=GENE_REVIEW.count_b, name="pairwiseOverlap__count_b", curie=GENE_REVIEW.curie('count_b'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__count_b, domain=None, range=int)

slots.pairwiseOverlap__intersection_count = Slot(uri=GENE_REVIEW.intersection_count, name="pairwiseOverlap__intersection_count", curie=GENE_REVIEW.curie('intersection_count'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__intersection_count, domain=None, range=int)

slots.pairwiseOverlap__a_minus_b_count = Slot(uri=GENE_REVIEW.a_minus_b_count, name="pairwiseOverlap__a_minus_b_count", curie=GENE_REVIEW.curie('a_minus_b_count'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__a_minus_b_count, domain=None, range=int)

slots.pairwiseOverlap__b_minus_a_count = Slot(uri=GENE_REVIEW.b_minus_a_count, name="pairwiseOverlap__b_minus_a_count", curie=GENE_REVIEW.curie('b_minus_a_count'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__b_minus_a_count, domain=None, range=int)

slots.pairwiseOverlap__jaccard_similarity = Slot(uri=GENE_REVIEW.jaccard_similarity, name="pairwiseOverlap__jaccard_similarity", curie=GENE_REVIEW.curie('jaccard_similarity'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__jaccard_similarity, domain=None, range=float)

slots.pairwiseOverlap__containment_a_in_b = Slot(uri=GENE_REVIEW.containment_a_in_b, name="pairwiseOverlap__containment_a_in_b", curie=GENE_REVIEW.curie('containment_a_in_b'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__containment_a_in_b, domain=None, range=float)

slots.pairwiseOverlap__containment_b_in_a = Slot(uri=GENE_REVIEW.containment_b_in_a, name="pairwiseOverlap__containment_b_in_a", curie=GENE_REVIEW.curie('containment_b_in_a'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__containment_b_in_a, domain=None, range=float)

slots.pairwiseOverlap__interpretation = Slot(uri=GENE_REVIEW.interpretation, name="pairwiseOverlap__interpretation", curie=GENE_REVIEW.curie('interpretation'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__interpretation, domain=None, range=Optional[Union[str, "OverlapInterpretationEnum"]])

slots.pairwiseOverlap__condition_a_in_sets = Slot(uri=GENE_REVIEW.condition_a_in_sets, name="pairwiseOverlap__condition_a_in_sets", curie=GENE_REVIEW.curie('condition_a_in_sets'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_a_in_sets, domain=None, range=Optional[Union[int, list[int]]])

slots.pairwiseOverlap__condition_b_in_sets = Slot(uri=GENE_REVIEW.condition_b_in_sets, name="pairwiseOverlap__condition_b_in_sets", curie=GENE_REVIEW.curie('condition_b_in_sets'),
                   model_uri=GENE_REVIEW.pairwiseOverlap__condition_b_in_sets, domain=None, range=Optional[Union[int, list[int]]])

slots.ruleReviewEntry__id = Slot(uri=GENE_REVIEW.id, name="ruleReviewEntry__id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__id, domain=None, range=URIRef)

slots.ruleReviewEntry__label = Slot(uri=GENE_REVIEW.label, name="ruleReviewEntry__label", curie=GENE_REVIEW.curie('label'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__label, domain=None, range=Optional[str])

slots.ruleReviewEntry__type = Slot(uri=GENE_REVIEW.type, name="ruleReviewEntry__type", curie=GENE_REVIEW.curie('type'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__type, domain=None, range=Union[str, "EntryTypeEnum"])

slots.ruleReviewEntry__appears_in_condition_sets = Slot(uri=GENE_REVIEW.appears_in_condition_sets, name="ruleReviewEntry__appears_in_condition_sets", curie=GENE_REVIEW.curie('appears_in_condition_sets'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__appears_in_condition_sets, domain=None, range=Optional[Union[int, list[int]]])

slots.ruleReviewEntry__protein_count = Slot(uri=GENE_REVIEW.protein_count, name="ruleReviewEntry__protein_count", curie=GENE_REVIEW.curie('protein_count'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__protein_count, domain=None, range=Optional[int])

slots.ruleReviewEntry__source = Slot(uri=GENE_REVIEW.source, name="ruleReviewEntry__source", curie=GENE_REVIEW.curie('source'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__source, domain=None, range=Optional[str])

slots.ruleReviewEntry__asserted_predicted_go_terms = Slot(uri=GENE_REVIEW.asserted_predicted_go_terms, name="ruleReviewEntry__asserted_predicted_go_terms", curie=GENE_REVIEW.curie('asserted_predicted_go_terms'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__asserted_predicted_go_terms, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleReviewEntry__related_entries = Slot(uri=GENE_REVIEW.related_entries, name="ruleReviewEntry__related_entries", curie=GENE_REVIEW.curie('related_entries'),
                   model_uri=GENE_REVIEW.ruleReviewEntry__related_entries, domain=None, range=Optional[Union[Union[dict, RelatedEntry], list[Union[dict, RelatedEntry]]]])

slots.relatedEntry__relationship = Slot(uri=GENE_REVIEW.relationship, name="relatedEntry__relationship", curie=GENE_REVIEW.curie('relationship'),
                   model_uri=GENE_REVIEW.relatedEntry__relationship, domain=None, range=Union[str, "EntryRelationshipEnum"])

slots.relatedEntry__target_id = Slot(uri=GENE_REVIEW.target_id, name="relatedEntry__target_id", curie=GENE_REVIEW.curie('target_id'),
                   model_uri=GENE_REVIEW.relatedEntry__target_id, domain=None, range=str)

slots.relatedEntry__containment = Slot(uri=GENE_REVIEW.containment, name="relatedEntry__containment", curie=GENE_REVIEW.curie('containment'),
                   model_uri=GENE_REVIEW.relatedEntry__containment, domain=None, range=Optional[float])

slots.relatedEntry__jaccard_similarity = Slot(uri=GENE_REVIEW.jaccard_similarity, name="relatedEntry__jaccard_similarity", curie=GENE_REVIEW.curie('jaccard_similarity'),
                   model_uri=GENE_REVIEW.relatedEntry__jaccard_similarity, domain=None, range=Optional[float])

slots.relatedEntry__intersection_count = Slot(uri=GENE_REVIEW.intersection_count, name="relatedEntry__intersection_count", curie=GENE_REVIEW.curie('intersection_count'),
                   model_uri=GENE_REVIEW.relatedEntry__intersection_count, domain=None, range=Optional[int])

slots.relatedEntry__exclusive_count = Slot(uri=GENE_REVIEW.exclusive_count, name="relatedEntry__exclusive_count", curie=GENE_REVIEW.curie('exclusive_count'),
                   model_uri=GENE_REVIEW.relatedEntry__exclusive_count, domain=None, range=Optional[int])

slots.interPro2GORedundancy__redundant_annotations = Slot(uri=GENE_REVIEW.redundant_annotations, name="interPro2GORedundancy__redundant_annotations", curie=GENE_REVIEW.curie('redundant_annotations'),
                   model_uri=GENE_REVIEW.interPro2GORedundancy__redundant_annotations, domain=None, range=Optional[Union[Union[dict, RedundantAnnotation], list[Union[dict, RedundantAnnotation]]]])

slots.interPro2GORedundancy__novel_annotations = Slot(uri=GENE_REVIEW.novel_annotations, name="interPro2GORedundancy__novel_annotations", curie=GENE_REVIEW.curie('novel_annotations'),
                   model_uri=GENE_REVIEW.interPro2GORedundancy__novel_annotations, domain=None, range=Optional[Union[str, list[str]]])

slots.interPro2GORedundancy__summary = Slot(uri=GENE_REVIEW.summary, name="interPro2GORedundancy__summary", curie=GENE_REVIEW.curie('summary'),
                   model_uri=GENE_REVIEW.interPro2GORedundancy__summary, domain=None, range=Optional[str])

slots.redundantAnnotation__go_id = Slot(uri=GENE_REVIEW.go_id, name="redundantAnnotation__go_id", curie=GENE_REVIEW.curie('go_id'),
                   model_uri=GENE_REVIEW.redundantAnnotation__go_id, domain=None, range=str)

slots.redundantAnnotation__go_label = Slot(uri=GENE_REVIEW.go_label, name="redundantAnnotation__go_label", curie=GENE_REVIEW.curie('go_label'),
                   model_uri=GENE_REVIEW.redundantAnnotation__go_label, domain=None, range=Optional[str])

slots.redundantAnnotation__interpro_source = Slot(uri=GENE_REVIEW.interpro_source, name="redundantAnnotation__interpro_source", curie=GENE_REVIEW.curie('interpro_source'),
                   model_uri=GENE_REVIEW.redundantAnnotation__interpro_source, domain=None, range=str)

slots.redundantAnnotation__interpro_label = Slot(uri=GENE_REVIEW.interpro_label, name="redundantAnnotation__interpro_label", curie=GENE_REVIEW.curie('interpro_label'),
                   model_uri=GENE_REVIEW.redundantAnnotation__interpro_label, domain=None, range=Optional[str])

slots.parsimonyAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="parsimonyAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.parsimonyAssessment__assessment, domain=None, range=Union[str, "ParsimonyEnum"])

slots.parsimonyAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="parsimonyAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.parsimonyAssessment__notes, domain=None, range=Optional[str])

slots.parsimonyAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="parsimonyAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.parsimonyAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.literatureSupportAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="literatureSupportAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.literatureSupportAssessment__assessment, domain=None, range=Union[str, "LiteratureSupportEnum"])

slots.literatureSupportAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="literatureSupportAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.literatureSupportAssessment__notes, domain=None, range=Optional[str])

slots.literatureSupportAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="literatureSupportAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.literatureSupportAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.conditionOverlapAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="conditionOverlapAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.conditionOverlapAssessment__assessment, domain=None, range=Union[str, "OverlapEnum"])

slots.conditionOverlapAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="conditionOverlapAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.conditionOverlapAssessment__notes, domain=None, range=Optional[str])

slots.conditionOverlapAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="conditionOverlapAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.conditionOverlapAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.gOSpecificityAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="gOSpecificityAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.gOSpecificityAssessment__assessment, domain=None, range=Union[str, "SpecificityEnum"])

slots.gOSpecificityAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="gOSpecificityAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.gOSpecificityAssessment__notes, domain=None, range=Optional[str])

slots.gOSpecificityAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="gOSpecificityAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.gOSpecificityAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.taxonomicScopeAssessment__assessment = Slot(uri=GENE_REVIEW.assessment, name="taxonomicScopeAssessment__assessment", curie=GENE_REVIEW.curie('assessment'),
                   model_uri=GENE_REVIEW.taxonomicScopeAssessment__assessment, domain=None, range=Union[str, "TaxonomicScopeEnum"])

slots.taxonomicScopeAssessment__notes = Slot(uri=GENE_REVIEW.notes, name="taxonomicScopeAssessment__notes", curie=GENE_REVIEW.curie('notes'),
                   model_uri=GENE_REVIEW.taxonomicScopeAssessment__notes, domain=None, range=Optional[str])

slots.taxonomicScopeAssessment__supported_by = Slot(uri=GENE_REVIEW.supported_by, name="taxonomicScopeAssessment__supported_by", curie=GENE_REVIEW.curie('supported_by'),
                   model_uri=GENE_REVIEW.taxonomicScopeAssessment__supported_by, domain=None, range=Optional[Union[Union[dict, SupportingTextInReference], list[Union[dict, SupportingTextInReference]]]])

slots.GeneReview_description = Slot(uri=DCTERMS.description, name="GeneReview_description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.GeneReview_description, domain=GeneReview, range=Optional[str])

slots.AlternativeProduct_id = Slot(uri=GENE_REVIEW.id, name="AlternativeProduct_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.AlternativeProduct_id, domain=AlternativeProduct, range=Union[str, AlternativeProductId])

slots.AlternativeProduct_name = Slot(uri=GENE_REVIEW.name, name="AlternativeProduct_name", curie=GENE_REVIEW.curie('name'),
                   model_uri=GENE_REVIEW.AlternativeProduct_name, domain=AlternativeProduct, range=Optional[str])

slots.AlternativeProduct_sequence_note = Slot(uri=GENE_REVIEW.sequence_note, name="AlternativeProduct_sequence_note", curie=GENE_REVIEW.curie('sequence_note'),
                   model_uri=GENE_REVIEW.AlternativeProduct_sequence_note, domain=AlternativeProduct, range=Optional[str])

slots.AlternativeProduct_description = Slot(uri=DCTERMS.description, name="AlternativeProduct_description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.AlternativeProduct_description, domain=AlternativeProduct, range=Optional[str])

slots.Term_id = Slot(uri=GENE_REVIEW.id, name="Term_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.Term_id, domain=Term, range=Union[str, TermId])

slots.Term_label = Slot(uri=RDFS.label, name="Term_label", curie=RDFS.curie('label'),
                   model_uri=GENE_REVIEW.Term_label, domain=Term, range=str)

slots.ExistingAnnotation_term = Slot(uri=GENE_REVIEW.term, name="ExistingAnnotation_term", curie=GENE_REVIEW.curie('term'),
                   model_uri=GENE_REVIEW.ExistingAnnotation_term, domain=ExistingAnnotation, range=Optional[Union[dict, Term]])

slots.CoreFunction_description = Slot(uri=DCTERMS.description, name="CoreFunction_description", curie=DCTERMS.curie('description'),
                   model_uri=GENE_REVIEW.CoreFunction_description, domain=CoreFunction, range=Optional[str])

slots.AnnotationExtension_predicate = Slot(uri=RDF.predicate, name="AnnotationExtension_predicate", curie=RDF.curie('predicate'),
                   model_uri=GENE_REVIEW.AnnotationExtension_predicate, domain=AnnotationExtension, range=str)

slots.RuleReview_id = Slot(uri=GENE_REVIEW.id, name="RuleReview_id", curie=GENE_REVIEW.curie('id'),
                   model_uri=GENE_REVIEW.RuleReview_id, domain=RuleReview, range=Union[str, RuleReviewId])
