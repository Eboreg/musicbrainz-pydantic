from __future__ import annotations

from collections.abc import Iterator
from typing import Annotated, Literal, Self

from pydantic import Discriminator, Field, Tag

from musicbrainz_pydantic.models import relations as r
from musicbrainz_pydantic.models.abstract import AbstractMBCoreEntity
from musicbrainz_pydantic.models.other import (
    MBAlias,
    MBArtistCredit,
    MBAttribute,
    MBLabelInfo,
    MBLifeSpan,
    MBMedium,
    MBRating,
    MBReleaseEvent,
    MBTag,
    MBTextRepresentation,
)
from musicbrainz_pydantic.utils import YearOrNone


class MBArea(AbstractMBCoreEntity):
    ENTITY_TYPE = "area"
    ENTITY_TYPE_PLURAL = "areas"
    INC_PARAMS = ("ratings",)
    INC_REQUIREMENTS = {
        "artist-credits": ("recording-rels", "release-rels", "release-group-rels"),
    }
    SEARCH_FIELDS = (
        "aid",
        "alias",
        "area",
        "areaaccent",
        "begin",
        "comment",
        "end",
        "iso",
        "iso1",
        "iso2",
        "iso3",
        "sortname",
        "tag",
        "type",
    )
    BOOLEAN_SEARCH_FIELDS = ("ended",)

    disambiguation: str
    name: str
    sort_name: str
    type: Literal[
        "City",
        "Country",
        "County",
        "District",
        "Island",
        "Municipality",
        "Subdivision",
    ] | None

    iso_3166_1_codes: list[str] = Field(default_factory=list)
    iso_3166_2_codes: list[str] = Field(default_factory=list)
    iso_3166_3_codes: list[str] = Field(default_factory=list)
    life_span: MBLifeSpan | None = None

    aliases: list[MBAlias] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBAreaAreaRelation
            | r.MBAreaEventRelation
            | r.MBAreaGenreRelation
            | r.MBAreaInstrumentRelation
            | r.MBAreaLabelRelation
            | r.MBAreaRecordingRelation
            | r.MBAreaReleaseRelation
            | r.MBAreaSeriesRelation
            | r.MBAreaUrlRelation
            | r.MBAreaWorkRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)


class MBArtist(AbstractMBCoreEntity):
    ENTITY_TYPE = "artist"
    ENTITY_TYPE_PLURAL = "artists"
    INC_PARAMS = (
        "discids",
        "isrcs",
        "media",
        "ratings",
        "recordings",
        "release-groups",
        "releases",
        "works",
    )
    INC_REQUIREMENTS = {
        "discids": ("releases",),
        "media": ("releases",),
        "isrcs": ("recordings",),
        "artist-credits": (
            "recording-rels",
            "recordings",
            "release-group-rels",
            "release-groups",
            "release-rels",
            "releases",
            "works",
        ),
    }
    # https://musicbrainz.org/doc/MusicBrainz_API/Search#Artist
    SEARCH_FIELDS = (
        "alias",
        "area",
        "arid",
        "artist",
        "artistaccent",
        "begin",
        "beginarea",
        "comment",
        "country",
        "end",
        "endarea",
        "ended",
        "gender",
        "ipi",
        "isni",
        "primary_alias",
        "sortname",
        "tag",
        "type",
    )
    BOOLEAN_SEARCH_FIELDS = ("ended",)

    country: str | None = None
    disambiguation: str | None = None
    gender: str | None = None
    name: str
    sort_name: str
    type: Literal["Character", "Choir", "Group", "Orchestra", "Other", "Person"] | None = None

    isnis: list[str] = Field(default_factory=list)
    life_span: MBLifeSpan | None = None
    rating: MBRating | None = None

    aliases: list["MBAlias"] = Field(default_factory=list)
    recordings: list["MBRecording"] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBArtistArtistRelation
            | r.MBArtistEventRelation
            | r.MBArtistGenreRelation
            | r.MBArtistInstrumentRelation
            | r.MBArtistLabelRelation
            | r.MBArtistPlaceRelation
            | r.MBArtistRecordingRelation
            | r.MBArtistReleaseRelation
            | r.MBArtistReleaseGroupRelation
            | r.MBArtistSeriesRelation
            | r.MBArtistUrlRelation
            | r.MBArtistWorkRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)
    release_groups: list["MBReleaseGroup"] = Field(default_factory=list)
    releases: list["MBRelease"] = Field(default_factory=list)
    tags: list["MBTag"] = Field(default_factory=list)
    works: list["MBWork"] = Field(default_factory=list)

    def get_discogs_id(self) -> str | None:
        for relation in self.relations:
            if relation.target_type == "url" and relation.type == "discogs":
                return relation.resource.strip("/").split("/")[-1]
        return None


class MBEvent(AbstractMBCoreEntity):
    ENTITY_TYPE = "event"
    ENTITY_TYPE_PLURAL = "events"
    INC_PARAMS = ("ratings",)
    INC_REQUIREMENTS = {"artist-credits": ("recording-rels", "release-group-rels", "release-rels")}
    SEARCH_FIELDS = (
        "aid",
        "alias",
        "area",
        "arid",
        "artist",
        "begin",
        "comment",
        "eid",
        "end",
        "event",
        "eventaccent",
        "pid",
        "place",
        "tag",
        "type",
    )
    BOOLEAN_SEARCH_FIELDS = ("ended",)

    cancelled: bool
    disambiguation: str
    life_span: MBLifeSpan | None = None
    name: str
    setlist: str
    time: str
    type: (
        Literal[
            "Award ceremony",
            "Concert",
            "Convention/Expo",
            "Festival",
            "Launch event",
            "Masterclass/Clinic",
            "Stage performance",
        ]
        | None
    ) = None

    aliases: list["MBAlias"] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBEventAreaRelation
            | r.MBEventArtistRelation
            | r.MBEventEventRelation
            | r.MBEventLabelRelation
            | r.MBEventPlaceRelation
            | r.MBEventRecordingRelation
            | r.MBEventReleaseGroupRelation
            | r.MBEventReleaseRelation
            | r.MBEventSeriesRelation
            | r.MBEventUrlRelation
            | r.MBEventWorkRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)


class MBLabel(AbstractMBCoreEntity):
    ENTITY_TYPE = "label"
    ENTITY_TYPE_PLURAL = "labels"
    INC_PARAMS = (
        "discids",
        "media",
        "ratings",
        "releases",
    )
    INC_REQUIREMENTS = {
        "discids": ("releases",),
        "media": ("releases",),
        "artist-credits": ("recording-rels", "release-group-rels", "release-rels", "releases"),
    }
    # https://musicbrainz.org/doc/MusicBrainz_API/Search#Label
    SEARCH_FIELDS = (
        "alias",
        "area",
        "begin",
        "code",
        "comment",
        "country",
        "end",
        "ended",
        "ipi",
        "isni",
        "label",
        "labelaccent",
        "laid",
        "release_count",
        "sortname",
        "tag",
        "type",
    )
    BOOLEAN_SEARCH_FIELDS = ("ended",)

    disambiguation: str | None = None
    label_code: int | None = None
    name: str
    sort_name: str | None = None
    type_id: str | None = None
    type: str | None = None

    aliases: list["MBAlias"] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBLabelAreaRelation
            | r.MBLabelArtistRelation
            | r.MBLabelEventRelation
            | r.MBLabelGenreRelation
            | r.MBLabelInstrumentRelation
            | r.MBLabelLabelRelation
            | r.MBLabelPlaceRelation
            | r.MBLabelRecordingRelation
            | r.MBLabelReleaseRelation
            | r.MBLabelReleaseGroupRelation
            | r.MBLabelSeriesRelation
            | r.MBLabelUrlRelation
            | r.MBLabelWorkRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)

    def get_discogs_id(self) -> str | None:
        for relation in self.relations:
            if relation.target_type == "url" and relation.type == "discogs":
                return relation.resource.strip("/").split("/")[-1]
        return None


class MBRecording(AbstractMBCoreEntity):
    ENTITY_TYPE = "recording"
    ENTITY_TYPE_PLURAL = "recordings"
    INC_PARAMS = (
        "artists",
        "discids",
        "isrcs",
        "media",
        "ratings",
        "release-groups",
        "releases",
        "work-level-rels",
    )
    INC_REQUIREMENTS = {
        "discids": ("releases",),
        "media": ("releases",),
    }
    # https://musicbrainz.org/doc/MusicBrainz_API/Search#Recording
    SEARCH_FIELDS = (
        "alias",
        "arid",  # the MBID of any of the recording artists
        "artist",
        "artistname",
        "comment",
        "country",
        "creditname",
        "date",
        "dur",  # the recording duration in milliseconds
        "firstreleasedate",
        "format",
        "isrc",
        "number",
        "position",
        "primarytype",
        "qdur",  # the recording duration, quantized (duration in milliseconds / 2000)
        "recording",
        "recordingaccent",
        "reid",  # the MBID of any release including this recording
        "release",
        "rgid",  # the MBID of any release group including this recording
        "rid",  # the recording's MBID
        "secondarytype",
        "status",
        "tag",
        "tid",  # the MBID of a track connected to this recording
        "tnum",
        "tracks",
        "tracksrelease",
        "type",
        "video",
    )
    BOOLEAN_SEARCH_FIELDS = ("video",)

    disambiguation: str | None = None
    first_release_date: YearOrNone = None
    length: int | None = None
    title: str
    video: bool | None = False

    isrcs: list[str] = Field(default_factory=list)
    rating: MBRating | None = None

    artist_credit: list[MBArtistCredit] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBRecordingAreaRelation
            | r.MBRecordingArtistRelation
            | r.MBRecordingEventRelation
            | r.MBRecordingLabelRelation
            | r.MBRecordingPlaceRelation
            | r.MBRecordingRecordingRelation
            | r.MBRecordingReleaseRelation
            | r.MBRecordingSeriesRelation
            | r.MBRecordingUrlRelation
            | r.MBRecordingWorkRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)
    releases: list["MBRelease"] = Field(default_factory=list)
    tags: list["MBTag"] = Field(default_factory=list)

    def get_date_best_guess(self):
        target_types = ["area", "place", "artist", "work"]  # in order of priority

        for target_type in target_types:
            lowest_date: str | None = None

            for relation in [rel for rel in self.relations if rel.target_type == target_type]:
                rel_date = relation.end or relation.begin
                if rel_date and (not lowest_date or lowest_date > rel_date):
                    lowest_date = rel_date

            if lowest_date:
                return lowest_date

        # first-release-date can be all kinds of weird sometimes,
        # that's why we use it as a last effort:
        return self.first_release_date


class MBRelease(AbstractMBCoreEntity):
    ENTITY_TYPE = "release"
    ENTITY_TYPE_PLURAL = "releases"
    INC_PARAMS = (
        "artists",
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
        "work-level-rels",
    )
    INC_REQUIREMENTS = {"isrcs": ("recordings",)}
    # https://musicbrainz.org/doc/MusicBrainz_API/Search#Release
    SEARCH_FIELDS = (
        "alias",
        "arid",  # the MBID of any of the release artists
        "artist",
        "artistname",
        "asin",
        "barcode",
        "catno",
        "comment",
        "country",
        "creditname",
        "date",
        "discids",
        "discidsmedium",
        "format",
        "label",
        "laid",  # the MBID of any of the release labels
        "lang",
        "mediumid",
        "mediums",  # the number of mediums on the release
        "packaging",
        "primarytype",
        "quality",
        "reid",  # the release's MBID
        "release",  # (part of) the release's title (diacritics are ignored)
        "releaseaccent",  # (part of) the release's title (with the specified diacritics)
        "rgid",  # the MBID of the release group for this release
        "script",
        "secondarytype",
        "status",
        "tag",
        "tracks",  # the total number of tracks on the release
        "tracksmedium",  # the number of tracks on any one medium on the release
        "type",
    )

    asin: str | None = None
    barcode: str | None = None
    country: str | None = None
    date: YearOrNone = None
    disambiguation: str | None = None
    packaging: str | None = None
    status: (
        Literal["Official", "Promotion", "Bootleg", "Pseudo-release", "Withdrawn", "Expunged", "Cancelled"] | None
    ) = None
    title: str
    track_count: int | None = None

    release_group: MBReleaseGroup | None = None
    text_representation: MBTextRepresentation | None = None

    artist_credit: list["MBArtistCredit"] = Field(default_factory=list)
    label_info: list[MBLabelInfo] = Field(default_factory=list)
    media: list[MBMedium] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBReleaseAreaRelation
            | r.MBReleaseArtistRelation
            | r.MBReleaseEventRelation
            | r.MBReleaseLabelRelation
            | r.MBReleasePlaceRelation
            | r.MBReleaseRecordingRelation
            | r.MBReleaseReleaseRelation
            | r.MBReleaseSeriesRelation
            | r.MBReleaseUrlRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)
    release_events: list["MBReleaseEvent"] = Field(default_factory=list)
    tags: list["MBTag"] = Field(default_factory=list)

    def get_album_artist_ids(self) -> list[str]:
        return list({rac.artist.id for rac in self.artist_credit})

    def get_artist(self) -> str:
        artist = ""
        for ac in self.artist_credit:
            if ac.joinphrase:
                artist += f"{ac.name}{ac.joinphrase}"
            else:
                artist += ac.name
        return artist

    def get_catalog_numbers(self) -> list[str]:
        return list({label_info.catalog_number for label_info in self.label_info if label_info.catalog_number})

    def get_discogs_id(self) -> str | None:
        # https://www.discogs.com/release/{id}
        for relation in self.relations:
            if relation.target_type == "url" and relation.type == "discogs":
                return relation.resource.strip("/").split("/")[-1]
        return None

    def get_discogs_master_id(self) -> str | None:
        return self.release_group.get_discogs_id() if self.release_group else None

    def get_earliest_release_date(self) -> str | None:
        release_dates: set[str] = set()

        if self.date:
            release_dates.add(self.date)
        if self.release_group and self.release_group.first_release_date:
            release_dates.add(self.release_group.first_release_date)

        return min(release_dates) if release_dates else None

    def get_is_various(self) -> bool:
        return self.get_artist().lower() == "various artists"

    def get_labels(self) -> list[str]:
        return list({label_info.label.name for label_info in self.label_info if label_info.label})

    @classmethod
    def discid_lookup(cls, toc: str, **kwargs) -> Iterator[Self]:
        yield from cls._browse("discid", id="-", toc=toc, **kwargs)


class MBReleaseGroup(AbstractMBCoreEntity):
    ENTITY_TYPE = "release-group"
    ENTITY_TYPE_PLURAL = "release-groups"
    INC_PARAMS = (
        "artists",
        "discids",
        "media",
        "ratings",
        "releases",
    )
    INC_REQUIREMENTS = {
        "discids": ("releases",),
        "media": ("releases",),
    }
    # https://musicbrainz.org/doc/MusicBrainz_API/Search#Release_Group
    SEARCH_FIELDS = (
        "alias",  # (part of) any alias attached to the release group (diacritics are ignored)
        "arid",  # the MBID of any of the release group artists
        "artist",  # (part of) the combined credited artist name for the release group, including join phrases
        "artistname",  # (part of) the name of any of the release group artists
        "comment",
        "creditname",
        "firstreleasedate",
        "primarytype",
        "reid",
        "release",  # the number of releases in the release group
        "releasegroup",
        "releasegroupaccent",
        "releases",
        "rgid",
        "secondarytype",
        "status",
        "tag",
        "type",
    )

    disambiguation: str | None = None
    first_release_date: YearOrNone = None
    primary_type: Literal["Album", "Broadcast", "EP", "Other", "Single"] | None = None
    title: str

    secondary_types: list[
        Literal[
            "Audio drama",
            "Audiobook",
            "Compilation",
            "Demo",
            "DJ-mix",
            "Field recording",
            "Interview",
            "Live",
            "Mixtape/Street",
            "Remix",
            "Soundtrack",
            "Spokenword",
        ]
    ] = Field(default_factory=list)

    artist_credit: list[MBArtistCredit] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBReleaseGroupArtistRelation
            | r.MBReleaseGroupEventRelation
            | r.MBReleaseGroupGenreRelation
            | r.MBReleaseGroupLabelRelation
            | r.MBReleaseGroupReleaseGroupRelation
            | r.MBReleaseGroupSeriesRelation
            | r.MBReleaseGroupUrlRelation
            | r.MBReleaseGroupWorkRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)
    releases: list[MBRelease] = Field(default_factory=list)

    def get_discogs_id(self) -> str | None:
        # https://www.discogs.com/master/{id}
        for relation in self.relations:
            if relation.target_type == "url" and relation.type == "discogs":
                return relation.resource.strip("/").split("/")[-1]
        return None


class MBSeries(AbstractMBCoreEntity):
    ENTITY_TYPE = "series"
    ENTITY_TYPE_PLURAL = "series"
    INC_REQUIREMENTS = {
        "artist-credits": ("recording-rels", "release-group-rels", "release-rels"),
    }
    # https://musicbrainz.org/doc/MusicBrainz_API/Search#Series
    SEARCH_FIELDS = (
        "alias",
        "comment",
        "series",
        "seriesaccent",
        "sid",
        "tag",
        "type",
    )

    disambiguation: str | None = None
    name: str
    type: str

    aliases: list["MBAlias"] = Field(default_factory=list)
    relations: list[
        Annotated[
            r.MBSeriesAreaRelation
            | r.MBSeriesArtistRelation
            | r.MBSeriesEventRelation
            | r.MBSeriesLabelRelation
            | r.MBSeriesPlaceRelation
            | r.MBSeriesRecordingRelation
            | r.MBSeriesReleaseGroupRelation
            | r.MBSeriesReleaseRelation
            | r.MBSeriesSeriesRelation
            | r.MBSeriesUrlRelation
            | r.MBSeriesWorkRelation,
            Field(discriminator="target_type"),
        ],
    ] = Field(default_factory=list)


def work_relation_discriminator(value):
    """
    This is because when doing a search for works
    (https://musicbrainz.org/doc/MusicBrainz_API/Search#Work), `relations`
    fields are returned that for some reason have no `target-type`, so we have
    to try and determine their types otherwise. Hopefully, this will not be
    necessary for any more models.
    """
    target_type = (
        value.get("target_type", value.get("target-type"))
        if isinstance(value, dict)
        else getattr(value, "target_type", None)
    )
    type = value.get("type") if isinstance(value, dict) else getattr(value, "type", None)

    if target_type:
        return target_type

    if type:
        for relation_type in (
            r.MBWorkAreaRelation,
            r.MBWorkArtistRelation,
            r.MBWorkEventRelation,
            r.MBWorkLabelRelation,
            r.MBWorkPlaceRelation,
            r.MBWorkRecordingRelation,
            r.MBWorkReleaseGroupRelation,
            r.MBWorkSeriesRelation,
            r.MBWorkUrlRelation,
            r.MBWorkWorkRelation,
        ):
            if type in relation_type.__annotations__["type"].__args__:
                for relation_subtype in [relation_type, *relation_type.__bases__]:
                    if "target_type" in relation_subtype.__annotations__:
                        return relation_subtype.__annotations__["target_type"].__args__[0]

    return None


class MBWork(AbstractMBCoreEntity):
    ENTITY_TYPE = "work"
    ENTITY_TYPE_PLURAL = "works"
    INC_PARAMS = ("ratings",)
    INC_REQUIREMENTS = {"artist-credits": ("recording-rels", "release-rels", "release-group-rels")}
    # https://musicbrainz.org/doc/MusicBrainz_API/Search#Work
    SEARCH_FIELDS = (
        "alias",
        "arid",
        "artist",
        "comment",
        "iswc",
        "lang",
        "recording_count",
        "recording",
        "rid",
        "tag",
        "type",
        "wid",
        "work",
        "workaccent",
    )

    language: str | None = None
    title: str
    type: str | None = None

    attributes: list[MBAttribute] = Field(default_factory=list)
    iswcs: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)

    relations: list[
        Annotated[
            Annotated[r.MBWorkAreaRelation, Tag("area")]
            | Annotated[r.MBWorkArtistRelation, Tag("artist")]
            | Annotated[r.MBWorkEventRelation, Tag("event")]
            | Annotated[r.MBWorkLabelRelation, Tag("label")]
            | Annotated[r.MBWorkPlaceRelation, Tag("place")]
            | Annotated[r.MBWorkRecordingRelation, Tag("recording")]
            | Annotated[r.MBWorkReleaseGroupRelation, Tag("release_group")]
            | Annotated[r.MBWorkSeriesRelation, Tag("series")]
            | Annotated[r.MBWorkUrlRelation, Tag("url")]
            | Annotated[r.MBWorkWorkRelation, Tag("work")],
            Discriminator(work_relation_discriminator),
        ],
    ] = Field(default_factory=list)

    def get_discogs_id(self) -> str | None:
        for relation in self.relations:
            if relation.target_type == "url" and relation.type == "discogs":
                return relation.resource.strip("/").split("/")[-1]
        return None


# These models are referenced in relation classes but were not available at
# the time of those classes' definition:
MBArea.model_rebuild()
MBArtist.model_rebuild()
MBEvent.model_rebuild()
MBLabel.model_rebuild()
MBRecording.model_rebuild()
MBRelease.model_rebuild()
MBReleaseGroup.model_rebuild()
MBSeries.model_rebuild()
MBWork.model_rebuild()
