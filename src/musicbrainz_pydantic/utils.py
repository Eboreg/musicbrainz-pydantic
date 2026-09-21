from __future__ import annotations

import re
from collections import namedtuple
from typing import TYPE_CHECKING, Annotated

from pydantic import AfterValidator

from musicbrainz_pydantic.exceptions import MBRequestError


if TYPE_CHECKING:
    from musicbrainz_pydantic.models.abstract import AbstractMBCoreEntity


YEAR_PATTERN = re.compile(r"^\d{4}")


def date_validator(value: str | None) -> str | None:
    if isinstance(value, str):
        value = value.strip()[:4]
        if len(value) < 4 or not YEAR_PATTERN.match(value):
            return None
    return value


def get_working_mbids_for_testing():
    Mbids = namedtuple("Mbids", "area, artist, event, label, recording, release, release_group, series, work")
    return Mbids(
        area="489ce91b-6658-3307-9877-795b68554c98",
        artist="230ca093-1d00-4c57-9235-147942f66930",
        event="157fc8ff-5638-48b0-99b6-fc0f33ef63e0",
        label="f18f3b31-8263-4de3-966a-fda317492d3d",
        recording="047ea438-f53e-4d21-b070-b0397b7e316e",
        release="f4a58037-2c36-44b1-84a9-4ad6e411b94f",
        release_group="a37fa623-d0f7-30b6-b646-25cab9bc1c92",
        series="1f49c45f-aa53-445b-9cc3-be483dd93e22",
        work="55c5fe9e-d965-4ff6-a2c9-f9fccfa6f17a",
    )


def lucene_escape(term: str):
    term = re.sub(r"([+\-!(){}\[\]^\"~*?:\\/])", r"\\\1", term)
    return term.replace("&&", "\\&&").replace("||", "\\||")


def test_inc_params(*models_with_mbids: tuple[type[AbstractMBCoreEntity], str]):
    from musicbrainz_pydantic.models.abstract import COMMON_INC_PARAMS

    other_inc_params = (
        "collections",
        "discids",
        "isrcs",
        "labels",
        "media",
        "ratings",
        "recording-level-rels",
        "recordings",
        "release-group-level-rels",
        "release-groups",
        "releases",
        "work-level-rels",
        "works",
    )
    incs = sorted(set([*COMMON_INC_PARAMS, *other_inc_params]))
    results: dict = {}

    for model, mbid in models_with_mbids:
        results[model.ENTITY_TYPE] = {"success": {"common": [], "other": []}, "failure": {}}
        for inc in incs:
            try:
                model.lookup(mbid, inc=inc, check_inc=False)
                if inc in COMMON_INC_PARAMS:
                    results[model.ENTITY_TYPE]["success"]["common"].append(inc)
                else:
                    results[model.ENTITY_TYPE]["success"]["other"].append(inc)
            except MBRequestError as e:
                results[model.ENTITY_TYPE]["failure"][inc] = e.error

    return results


YearOrNone = Annotated[str | None, AfterValidator(date_validator)]
