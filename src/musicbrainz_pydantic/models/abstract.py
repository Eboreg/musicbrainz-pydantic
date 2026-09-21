from __future__ import annotations

import re
from abc import ABC
from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING, Any, ClassVar, Literal, Self

from klaatu_python.utils import fancy_join, is_truthy
from pydantic import AliasPath, Field

from musicbrainz_pydantic import logger
from musicbrainz_pydantic.models.base import AbstractBaseMBModel
from musicbrainz_pydantic.models.shelf import get_from_shelf, save_to_shelf
from musicbrainz_pydantic.request import request
from musicbrainz_pydantic.utils import YearOrNone, lucene_escape


if TYPE_CHECKING:
    import logging

    from musicbrainz_pydantic.models.core import (
        MBArea,
        MBArtist,
        MBEvent,
        MBLabel,
        MBRecording,
        MBRelease,
        MBReleaseGroup,
        MBSeries,
        MBWork,
    )


COMMON_INC_PARAMS = (
    "aliases",
    "annotation",
    "artist-credits",
    "genres",
    "tags",
)

REL_INC_PARAMS = (
    "area-rels",
    "artist-rels",
    "event-rels",
    "genre-rels",
    "instrument-rels",
    "label-rels",
    "place-rels",
    "recording-rels",
    "release-group-rels",
    "release-rels",
    "series-rels",
    "url-rels",
    "work-rels",
)


class AbstractMBCoreEntity(AbstractBaseMBModel, ABC):
    BOOLEAN_SEARCH_FIELDS: ClassVar[Iterable[str]] = []
    ENTITY_TYPE_PLURAL: ClassVar[str]
    ENTITY_TYPE: ClassVar[str]
    INC_PARAMS: ClassVar[Iterable[str]] = []
    INC_REQUIREMENTS: ClassVar[dict[str, Iterable[str]]] = {}
    SEARCH_FIELDS: ClassVar[Iterable[str]]

    id: str

    @classmethod
    def _browse(
        cls,
        resource: str,
        links: dict[str, str] | None = None,
        inc: str | Iterable = "",
        logger: logging.Logger = logger,
        check_inc: bool = True,
        **kwargs,
    ) -> Iterator[Self]:
        incs = cls._normalize_inc(inc)
        if check_inc:
            cls.check_inc(incs)
        links = links or {}
        limit = int(kwargs.pop("limit", 100))
        offset: int | None = int(kwargs.pop("offset", 0))
        params = {"limit": limit, "inc": " ".join(incs), **links, **kwargs}

        while offset is not None:
            params["offset"] = offset
            response = request(resource, logger=logger, **params)
            entity_jsons = response.get(cls.ENTITY_TYPE_PLURAL, [])
            entity_count = response.get(f"{cls.ENTITY_TYPE}-count")
            if isinstance(entity_count, int) and entity_count > offset + len(entity_jsons):
                offset += len(entity_jsons)
            else:
                offset = None
            for entity_json in entity_jsons:
                save_to_shelf(cls.ENTITY_TYPE, entity_json["id"], incs, entity_json)
                yield cls.model_validate(entity_json)

    @staticmethod
    def _normalize_inc(inc: str | Iterable) -> list[str]:
        if isinstance(inc, str):
            inc = inc.strip()
            if not inc:
                return []
            incs = re.split(r" +", inc)
        else:
            incs = [str(i).strip() for i in inc]
        return sorted(set(incs))

    @classmethod
    def browse(
        cls,
        links: dict[str, str] | None = None,
        inc: str | Iterable = "",
        logger: logging.Logger = logger,
        check_inc: bool = True,
        **kwargs,
    ) -> Iterator[Self]:
        yield from cls._browse(cls.ENTITY_TYPE, links=links, inc=inc, logger=logger, check_inc=check_inc, **kwargs)

    @classmethod
    def check_inc(cls, incs: list[str]):
        valid_incs = cls.get_valid_inc_params()
        for inc in incs:
            assert inc in valid_incs, f"{inc} is not one of the valid inc parameters: {valid_incs}"
        for inc, others in cls.INC_REQUIREMENTS.items():
            if inc in incs:
                assert any(m in incs for m in others), f"{inc} can only be in inc if {fancy_join(others, 'or')} also is"

    @classmethod
    def get_valid_inc_params(cls) -> list[str]:
        return sorted({*COMMON_INC_PARAMS, *REL_INC_PARAMS, *cls.INC_PARAMS})

    @classmethod
    def lookup(
        cls,
        id: str,
        inc: str | Iterable = "",
        logger: logging.Logger = logger,
        check_inc: bool = True,
        ignore_cache: bool = False,
        **kwargs,
    ) -> Self:
        incs = cls._normalize_inc(inc)
        if check_inc:
            cls.check_inc(incs)
        entity_json = get_from_shelf(cls.ENTITY_TYPE, id, incs) if not ignore_cache else None
        if not entity_json:
            entity_json = request(cls.ENTITY_TYPE, id=id, inc=" ".join(incs), logger=logger, **kwargs)
            save_to_shelf(cls.ENTITY_TYPE, id, incs, entity_json)
        return cls.model_validate(entity_json)

    @classmethod
    def search(cls, freetext: str | None = None, params: dict[str, Any] | None = None, **kwargs) -> Iterator[Self]:
        params = params or {}
        limit = int(kwargs.pop("limit", 100))
        offset: int | None = int(kwargs.pop("offset", 0))
        and_queries = []
        not_queries = []

        if freetext:
            and_queries.append(f'"{lucene_escape(freetext)}"' if " " in freetext else lucene_escape(freetext))

        for key, value in params.items():
            queries = and_queries
            if key.startswith("-"):
                key = key[1:]
                queries = not_queries
            if key in cls.SEARCH_FIELDS:
                if key in cls.BOOLEAN_SEARCH_FIELDS:
                    queries.append(f"{key}:{'true' if is_truthy(value) else 'false'}")
                elif value is None:
                    queries.append(f"-{key}:*")
                else:
                    escaped_value = lucene_escape(value)
                    if " " in value:
                        escaped_value = f'"{escaped_value}"'
                    queries.append(f"{key}:{escaped_value}")

        query = " AND ".join(and_queries)
        if not_queries:
            query += " NOT " + " NOT ".join(not_queries)
        request_params = {"query": query, "limit": limit, **kwargs}

        while offset is not None:
            request_params["offset"] = offset
            response = request(cls.ENTITY_TYPE, **request_params)
            entities = response.get(cls.ENTITY_TYPE_PLURAL, [])
            entity_count = response.get("count")
            if isinstance(entity_count, int) and entity_count > offset + len(entities):
                offset += len(entities)
            else:
                offset = None
            for entity in entities:
                yield cls.model_validate(entity)


class AbstractMBRelation(AbstractBaseMBModel, ABC):
    begin: YearOrNone = None
    direction: Literal["backward", "forward"]
    end: YearOrNone = None
    ended: bool | None = None

    attribute_ids: dict[str, str] = Field(default_factory=dict)
    attribute_values: dict[str, str] = Field(default_factory=dict)
    attributes: list[str] = Field(default_factory=list)


class AbstractMBAreaRelation(AbstractMBRelation, ABC):
    area: MBArea
    target_type: Literal["area"] = "area"


class AbstractMBArtistRelation(AbstractMBRelation, ABC):
    artist: MBArtist
    target_type: Literal["artist"] = "artist"


class AbstractMBEventRelation(AbstractMBRelation, ABC):
    event: MBEvent
    target_type: Literal["event"] = "event"


class AbstractMBGenreRelation(AbstractMBRelation, ABC):
    target_type: Literal["genre"] = "genre"


class AbstractMBInstrumentRelation(AbstractMBRelation, ABC):
    target_type: Literal["instrument"] = "instrument"


class AbstractMBLabelRelation(AbstractMBRelation, ABC):
    label: MBLabel
    target_type: Literal["label"] = "label"


class AbstractMBPlaceRelation(AbstractMBRelation, ABC):
    target_type: Literal["place"] = "place"


class AbstractMBRecordingRelation(AbstractMBRelation, ABC):
    recording: MBRecording
    target_type: Literal["recording"] = "recording"


class AbstractMBReleaseRelation(AbstractMBRelation, ABC):
    release: MBRelease
    target_type: Literal["release"] = "release"


class AbstractMBReleaseGroupRelation(AbstractMBRelation, ABC):
    release_group: MBReleaseGroup
    target_type: Literal["release_group"] = "release_group"


class AbstractMBSeriesRelation(AbstractMBRelation, ABC):
    ordering_key: int | None = None
    series: MBSeries
    target_type: Literal["series"] = "series"


class AbstractMBUrlRelation(AbstractMBRelation, ABC):
    resource: str = Field(validation_alias=AliasPath("url", "resource"))
    target_type: Literal["url"] = "url"


class AbstractMBWorkRelation(AbstractMBRelation, ABC):
    target_type: Literal["work"] = "work"
    work: MBWork
