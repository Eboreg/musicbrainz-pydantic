from typing import Literal

from musicbrainz_pydantic.models.abstract import (
    AbstractMBAreaRelation,
    AbstractMBArtistRelation,
    AbstractMBEventRelation,
    AbstractMBGenreRelation,
    AbstractMBInstrumentRelation,
    AbstractMBLabelRelation,
    AbstractMBPlaceRelation,
    AbstractMBRecordingRelation,
    AbstractMBReleaseGroupRelation,
    AbstractMBReleaseRelation,
    AbstractMBSeriesRelation,
    AbstractMBUrlRelation,
    AbstractMBWorkRelation,
)


AreaEventRelationType = Literal["held in"]

AreaGenreRelationType = Literal["genre origin", "named after area"]

AreaInstrumentRelationType = Literal["instrument origin"]

AreaLabelRelationType = Literal["headquarters"]

AreaRecordingRelationType = Literal[
    "arranged in",
    "edited in",
    "engineered in",
    "mixed in",
    "produced in",
    "recorded in",
    "remixed in",
    "video shot in",
]

AreaReleaseRelationType = Literal[
    "arranged in",
    "composed in",
    "edited in",
    "engineered in",
    "lacquer cut in",
    "libretto written in",
    "lyrics written in",
    "manufactured in",
    "mastered in",
    "mixed in",
    "printed in",
    "produced in",
    "recorded in",
    "remixed in",
    "revised in",
    "transferred in",
    "translated in",
    "written in",
]

AreaSeriesRelationType = Literal["held in"]

AreaUrlRelationType = Literal["geonames", "other databases", "wikidata", "wikipedia"]

AreaWorkRelationType = Literal[
    "anthem",
    "arranged in",
    "commissioned",
    "composed in",
    "dedication",
    "libretto written in",
    "lyrics written in",
    "premiere",
    "revised in",
    "translated in",
    "written in",
]

ArtistEventRelationType = Literal[
    "artwork",
    "conductor",
    "design",
    "engineer",
    "graphic design",
    "guest performer",
    "host",
    "illustration",
    "jury member",
    "main performer",
    "orchestra",
    "participant",
    "support act",
    "supporting DJ",
    "teacher",
    "tribute to",
    "VJ",
]

ArtistGenreRelationType = Literal["named after artist"]

ArtistInstrumentRelationType = Literal["invented"]

ArtistLabelRelationType = Literal[
    "artists and repertoire position at",
    "creative position at",
    "engineer position at",
    "executive position at",
    "label founder",
    "named after artist",
    "named after label",
    "owner",
    "personal label",
    "personal publisher",
    "position at",
    "producer position at",
    "recording contract",
]

ArtistPlaceRelationType = Literal[
    "artist-in-residence",
    "associated with",
    "carillonneur",
    "composer-in-residence",
    "engineer position",
    "founder",
    "mastering engineer position",
    "mixing engineer position",
    "named after artist",
    "named after place",
    "organist",
    "owner",
    "primary concert venue",
    "recording engineer position",
    "school director at",
    "studied at",
    "taught at",
]

ArtistRecordingRelationType = Literal[
    "animation",
    "arranger",
    "art direction",
    "artists and repertoire",
    "artwork",
    "audio director",
    "audio",
    "balance",
    "booking",
    "choreographer",
    "chorus master",
    "cinematographer",
    "compiler",
    "concertmaster",
    "conductor",
    "creative direction",
    "dedication",
    "design",
    "design/illustration",
    "editor",
    "engineer",
    "field recordist",
    "graphic design",
    "illustration",
    "instrument arranger",
    "instrument technician",
    "instrument",
    "legal representation",
    "mastering",
    "misc",
    "mix-DJ",
    "mix",
    "orchestrator",
    "performer",
    "performing orchestra",
    "phonographic copyright",
    "photography",
    "producer",
    "programming",
    "publishing",
    "recording",
    "remixer",
    "samples from artist",
    "sound effects",
    "sound",
    "video appearance",
    "video copyright",
    "video director",
    "vocal arranger",
    "vocal",
]

ArtistReleaseRelationType = Literal[
    "arranger",
    "art direction",
    "artwork",
    "audio director",
    "audio",
    "balance",
    "booking",
    "booklet editor",
    "chorus master",
    "compiler",
    "composer",
    "concertmaster",
    "conductor",
    "copyright",
    "design",
    "design/illustration",
    "editor",
    "engineer",
    "field recordist",
    "graphic design",
    "illustration",
    "instrument arranger",
    "instrument technician",
    "instrument",
    "lacquer cut",
    "legal representation",
    "librettist",
    "licensor",
    "liner notes",
    "lyricist",
    "mastering",
    "misc",
    "mix-DJ",
    "mix",
    "orchestrator",
    "performer",
    "performing orchestra",
    "phonographic copyright",
    "photography",
    "producer",
    "production coordinator",
    "programming",
    "publishing",
    "recording",
    "remixer",
    "samples from artist",
    "sound effects",
    "sound",
    "transfer",
    "translator",
    "video director",
    "vocal arranger",
    "vocal",
    "writer",
]

ArtistReleaseGroupRelationType = Literal[
    "artists and repertoire",
    "creative direction",
    "dedicated to",
    "named after release group",
    "tribute",
]

ArtistSeriesRelationType = Literal[
    "catalogued",
    "founder",
    "has catalogue",
    "host",
    "named after artist",
    "part of",
    "residency",
    "tour",
]

ArtistUrlRelationType = Literal[
    "allmusic",
    "apple music",
    "art gallery",
    "bandcamp",
    "bandsintown",
    "BBC Music page",
    "biography",
    "blog",
    "BookBrainz",
    "CD Baby",
    "CPDL",
    "crowdfunding",
    "discography page",
    "discogs",
    "download for free",
    "fanpage",
    "free streaming",
    "image",
    "IMDb",
    "IMSLP",
    "interview",
    "last.fm",
    "lyrics",
    "myspace",
    "official homepage",
    "online community",
    "other databases",
    "patronage",
    "purchase for download",
    "purchase for mail-order",
    "purevolume",
    "secondhandsongs",
    "setlistfm",
    "social network",
    "songkick",
    "soundcloud",
    "streaming",
    "ticketing",
    "vgmdb",
    "VIAF",
    "video channel",
    "wikidata",
    "wikipedia",
    "youtube music",
    "youtube",
]

ArtistWorkRelationType = Literal[
    "adapter",
    "arranger",
    "choreographer",
    "commissioned",
    "composer",
    "dedication",
    "instrument arranger",
    "librettist",
    "lyricist",
    "misc",
    "named after artist",
    "named after work",
    "orchestrator",
    "premiere",
    "previous attribution",
    "publishing",
    "reconstructed by",
    "revised by",
    "scriptwriter",
    "translator",
    "vocal arranger",
    "writer",
]

EventLabelRelationType = Literal["presented"]

EventPlaceRelationType = Literal["held at"]

EventRecordingRelationType = Literal["recorded at", "video shot at"]

EventReleaseRelationType = Literal["available at", "launch event", "recorded at"]

EventReleaseGroupRelationType = Literal["launch event", "performance of"]

EventSeriesRelationType = Literal["part of"]

EventUrlRelationType = Literal[
    "bandsintown",
    "crowdfunding",
    "discogs",
    "fanpage",
    "last.fm",
    "official homepage",
    "other databases",
    "patronage",
    "poster",
    "purchase artwork",
    "review",
    "schedule",
    "setlistfm",
    "social network",
    "songkick",
    "ticketing",
    "vgmdb",
    "video channel",
    "wikidata",
    "wikipedia",
    "youtube",
]

EventWorkRelationType = Literal["premiere"]

GenreLabelRelationType = Literal["named after label"]

GenreReleaseGroupRelationType = Literal["named after release group"]

InstrumentLabelRelationType = Literal["invented"]

LabelPlaceRelationType = Literal["owner"]

LabelRecordingRelationType = Literal[
    "arranged for",
    "broadcast",
    "edited for",
    "misc",
    "mix",
    "mixed for",
    "phonographic copyright",
    "produced for",
    "publishing",
    "recording",
    "remixed for",
    "video copyright",
]

LabelReleaseRelationType = Literal[
    "arranged for",
    "art direction",
    "artwork",
    "copyright",
    "design",
    "distributed",
    "edited for",
    "exported",
    "glass mastered",
    "graphic design",
    "illustration",
    "licensee",
    "licensor",
    "manufactured for",
    "manufactured",
    "marketed",
    "mastered for",
    "mastering",
    "misc",
    "mix",
    "mixed for",
    "phonographic copyright",
    "photography",
    "pressed",
    "printed",
    "produced for",
    "promoted",
    "published",
    "rights society",
]

LabelReleaseGroupRelationType = Literal["tribute"]

LabelSeriesRelationType = Literal["publishes series"]

LabelUrlRelationType = Literal[
    "apple music",
    "bandcamp",
    "blog",
    "BookBrainz",
    "catalog site",
    "crowdfunding",
    "discogs",
    "download for free",
    "fanpage",
    "free streaming",
    "history site",
    "IMDb",
    "last.fm",
    "logo",
    "lyrics",
    "myspace",
    "official site",
    "other databases",
    "patronage",
    "purchase for download",
    "purchase for mail-order",
    "secondhandsongs",
    "social network",
    "soundcloud",
    "streaming",
    "ticketing",
    "vgmdb",
    "VIAF",
    "video channel",
    "wikidata",
    "wikipedia",
    "youtube",
]

LabelWorkRelationType = Literal["commissioned", "dedication", "named after work", "publishing"]

PlaceRecordingRelationType = Literal[
    "arranged at",
    "edited at",
    "engineered at",
    "mixed at",
    "produced at",
    "recorded at",
    "remixed at",
    "video shot at",
]

PlaceReleaseRelationType = Literal[
    "arranged at",
    "composed at",
    "edited at",
    "engineered at",
    "glass mastered at",
    "lacquer cut at",
    "libretto written at",
    "lyrics written at",
    "manufactured at",
    "mastered at",
    "mixed at",
    "pressed at",
    "produced at",
    "recorded at",
    "remixed at",
    "revised at",
    "transferred at",
    "translated at",
    "written at",
]

PlaceSeriesRelationType = Literal["held at"]

PlaceWorkRelationType = Literal[
    "arranged at",
    "commissioned",
    "composed at",
    "dedication",
    "libretto written at",
    "lyrics written at",
    "premiere",
    "revised at",
    "translated at",
    "written at",
]

RecordingReleaseRelationType = Literal["samples material"]

RecordingSeriesRelationType = Literal["part of", "recorded during"]

RecordingUrlRelationType = Literal[
    "allmusic",
    "crowdfunding",
    "download for free",
    "free streaming",
    "IMDB samples",
    "license",
    "other databases",
    "purchase for download",
    "secondhandsongs",
    "streaming",
]

RecordingWorkRelationType = Literal["performance"]

ReleaseSeriesRelationType = Literal["part of"]

ReleaseUrlRelationType = Literal[
    "allmusic",
    "amazon asin",
    "BookBrainz",
    "cover art link",
    "crowdfunding",
    "discography entry",
    "discogs",
    "download for free",
    "free streaming",
    "IMDB samples",
    "license",
    "other databases",
    "purchase for download",
    "purchase for mail-order",
    "secondhandsongs",
    "show notes",
    "streaming",
    "vgmdb",
]

ReleaseGroupSeriesRelationType = Literal[
    "named after release group",
    "part of",
    "recorded during",
    "tour in support of",
]

ReleaseGroupUrlRelationType = Literal[
    "allmusic",
    "BookBrainz",
    "crowdfunding",
    "discography entry",
    "discography",
    "discogs",
    "fanpage",
    "IMDb",
    "lyrics",
    "official homepage",
    "other databases",
    "review",
    "wikidata",
    "wikipedia",
]

ReleaseGroupWorkRelationType = Literal["named after work"]

SeriesUrlRelationType = Literal[
    "BookBrainz",
    "crowdfunding",
    "discogs",
    "fanpage",
    "IMDb",
    "logo",
    "official homepage",
    "other databases",
    "patronage",
    "podcast feed",
    "schedule",
    "setlistfm",
    "social network",
    "soundcloud",
    "ticketing",
    "VIAF",
    "video channel",
    "wikidata",
    "wikipedia",
    "youtube",
]

SeriesWorkRelationType = Literal["commissioned", "part of"]

UrlWorkRelationType = Literal[
    "allmusic",
    "BookBrainz",
    "crowdfunding",
    "discogs",
    "download for free",
    "fanpage",
    "IMDb",
    "license",
    "lyrics",
    "other databases",
    "purchase for download",
    "purchase for mail-order",
    "secondhandsongs",
    "songfacts",
    "vgmdb",
    "VIAF",
    "wikidata",
    "wikipedia",
    "work list entry",
]


class MBAreaAreaRelation(AbstractMBAreaRelation):
    type: Literal["part of"]


class MBAreaEventRelation(AbstractMBEventRelation):
    type: AreaEventRelationType


class MBAreaGenreRelation(AbstractMBGenreRelation):
    type: AreaGenreRelationType


class MBAreaInstrumentRelation(AbstractMBInstrumentRelation):
    type: AreaInstrumentRelationType


class MBAreaLabelRelation(AbstractMBLabelRelation):
    type: AreaLabelRelationType


class MBAreaRecordingRelation(AbstractMBRecordingRelation):
    type: AreaRecordingRelationType


class MBAreaReleaseRelation(AbstractMBReleaseRelation):
    type: AreaReleaseRelationType


class MBAreaSeriesRelation(AbstractMBSeriesRelation):
    type: AreaSeriesRelationType


class MBAreaUrlRelation(AbstractMBUrlRelation):
    type: AreaUrlRelationType


class MBAreaWorkRelation(AbstractMBWorkRelation):
    type: AreaWorkRelationType


class MBArtistArtistRelation(AbstractMBArtistRelation):
    type: Literal[
        "artist rename",
        "artist-in-residence",
        "artistic director",
        "collaboration",
        "composer-in-residence",
        "conductor position",
        "founder",
        "instrumental supporting musician",
        "involved with",
        "is person",
        "married",
        "member of band",
        "named after artist",
        "parent",
        "sibling",
        "subgroup",
        "supporting musician",
        "teacher",
        "tribute",
        "vocal supporting musician",
        "voice actor",
    ]


class MBArtistEventRelation(AbstractMBEventRelation):
    type: ArtistEventRelationType


class MBArtistGenreRelation(AbstractMBGenreRelation):
    type: ArtistGenreRelationType


class MBArtistInstrumentRelation(AbstractMBInstrumentRelation):
    type: ArtistInstrumentRelationType


class MBArtistLabelRelation(AbstractMBLabelRelation):
    type: ArtistLabelRelationType


class MBArtistPlaceRelation(AbstractMBPlaceRelation):
    type: ArtistPlaceRelationType


class MBArtistRecordingRelation(AbstractMBRecordingRelation):
    type: ArtistRecordingRelationType


class MBArtistReleaseRelation(AbstractMBReleaseRelation):
    type: ArtistReleaseRelationType


class MBArtistReleaseGroupRelation(AbstractMBReleaseGroupRelation):
    type: ArtistReleaseGroupRelationType


class MBArtistSeriesRelation(AbstractMBSeriesRelation):
    type: ArtistSeriesRelationType


class MBArtistUrlRelation(AbstractMBUrlRelation):
    type: ArtistUrlRelationType


class MBArtistWorkRelation(AbstractMBWorkRelation):
    type: ArtistWorkRelationType


class MBEventAreaRelation(AbstractMBAreaRelation):
    type: AreaEventRelationType


class MBEventArtistRelation(AbstractMBArtistRelation):
    type: ArtistEventRelationType


class MBEventEventRelation(AbstractMBEventRelation):
    type: Literal["parts", "rescheduled as"]


class MBEventLabelRelation(AbstractMBLabelRelation):
    type: EventLabelRelationType


class MBEventPlaceRelation(AbstractMBPlaceRelation):
    type: EventPlaceRelationType


class MBEventRecordingRelation(AbstractMBRecordingRelation):
    type: EventRecordingRelationType


class MBEventReleaseRelation(AbstractMBReleaseRelation):
    type: EventReleaseRelationType


class MBEventReleaseGroupRelation(AbstractMBReleaseGroupRelation):
    type: EventReleaseGroupRelationType


class MBEventSeriesRelation(AbstractMBSeriesRelation):
    type: EventSeriesRelationType


class MBEventUrlRelation(AbstractMBUrlRelation):
    type: EventUrlRelationType


class MBEventWorkRelation(AbstractMBWorkRelation):
    type: EventWorkRelationType


class MBLabelAreaRelation(AbstractMBAreaRelation):
    type: AreaLabelRelationType


class MBLabelArtistRelation(AbstractMBArtistRelation):
    type: ArtistLabelRelationType


class MBLabelEventRelation(AbstractMBEventRelation):
    type: EventLabelRelationType


class MBLabelGenreRelation(AbstractMBGenreRelation):
    type: GenreLabelRelationType


class MBLabelInstrumentRelation(AbstractMBInstrumentRelation):
    type: InstrumentLabelRelationType


class MBLabelLabelRelation(AbstractMBLabelRelation):
    type: Literal[
        "imprint",
        "label distribution",
        "label ownership",
        "label reissue",
        "label rename",
    ]


class MBLabelPlaceRelation(AbstractMBPlaceRelation):
    type: LabelPlaceRelationType


class MBLabelRecordingRelation(AbstractMBRecordingRelation):
    type: LabelRecordingRelationType


class MBLabelReleaseRelation(AbstractMBReleaseRelation):
    type: LabelReleaseRelationType


class MBLabelReleaseGroupRelation(AbstractMBReleaseGroupRelation):
    type: LabelReleaseGroupRelationType


class MBLabelSeriesRelation(AbstractMBSeriesRelation):
    type: LabelSeriesRelationType


class MBLabelUrlRelation(AbstractMBUrlRelation):
    type: LabelUrlRelationType


class MBLabelWorkRelation(AbstractMBWorkRelation):
    type: LabelWorkRelationType


class MBRecordingAreaRelation(AbstractMBAreaRelation):
    type: AreaRecordingRelationType


class MBRecordingArtistRelation(AbstractMBArtistRelation):
    type: ArtistRecordingRelationType


class MBRecordingEventRelation(AbstractMBEventRelation):
    type: EventRecordingRelationType


class MBRecordingLabelRelation(AbstractMBLabelRelation):
    type: LabelRecordingRelationType


class MBRecordingPlaceRelation(AbstractMBPlaceRelation):
    type: PlaceRecordingRelationType


class MBRecordingRecordingRelation(AbstractMBRecordingRelation):
    type: Literal[
        "a cappella",
        "commentary",
        "compilation",
        "DJ-mix",
        "edit",
        "first track release",
        "instrumental",
        "karaoke",
        "mashes up",
        "music video",
        "remaster",
        "remix",
        "samples material",
    ]


class MBRecordingReleaseRelation(AbstractMBReleaseRelation):
    type: RecordingReleaseRelationType


class MBRecordingSeriesRelation(AbstractMBSeriesRelation):
    type: RecordingSeriesRelationType


class MBRecordingUrlRelation(AbstractMBUrlRelation):
    type: RecordingUrlRelationType


class MBRecordingWorkRelation(AbstractMBWorkRelation):
    type: RecordingWorkRelationType


class MBReleaseAreaRelation(AbstractMBAreaRelation):
    type: AreaReleaseRelationType


class MBReleaseArtistRelation(AbstractMBArtistRelation):
    type: ArtistReleaseRelationType


class MBReleaseEventRelation(AbstractMBEventRelation):
    type: EventReleaseRelationType


class MBReleaseLabelRelation(AbstractMBLabelRelation):
    type: LabelReleaseRelationType


class MBReleasePlaceRelation(AbstractMBPlaceRelation):
    type: PlaceReleaseRelationType


class MBReleaseRecordingRelation(AbstractMBRecordingRelation):
    type: RecordingReleaseRelationType


class MBReleaseReleaseRelation(AbstractMBReleaseRelation):
    type: Literal[
        "part of set",
        "remaster",
        "replaced by",
        "supporting release",
        "transl-tracklisting",
    ]


class MBReleaseSeriesRelation(AbstractMBSeriesRelation):
    type: ReleaseSeriesRelationType


class MBReleaseUrlRelation(AbstractMBUrlRelation):
    type: ReleaseUrlRelationType


class MBReleaseGroupArtistRelation(AbstractMBArtistRelation):
    type: ArtistReleaseGroupRelationType


class MBReleaseGroupEventRelation(AbstractMBEventRelation):
    type: EventReleaseGroupRelationType


class MBReleaseGroupGenreRelation(AbstractMBGenreRelation):
    type: GenreReleaseGroupRelationType


class MBReleaseGroupLabelRelation(AbstractMBLabelRelation):
    type: LabelReleaseGroupRelationType


class MBReleaseGroupReleaseGroupRelation(AbstractMBReleaseGroupRelation):
    type: Literal[
        "commentary",
        "cover",
        "DJ-mix",
        "excerpt from",
        "included in",
        "live performance",
        "mashes up",
        "re-recording",
        "remix",
        "single from",
        "translated version",
    ]


class MBReleaseGroupSeriesRelation(AbstractMBSeriesRelation):
    type: ReleaseGroupSeriesRelationType


class MBReleaseGroupUrlRelation(AbstractMBUrlRelation):
    type: ReleaseGroupUrlRelationType


class MBReleaseGroupWorkRelation(AbstractMBWorkRelation):
    type: ReleaseGroupWorkRelationType


class MBSeriesAreaRelation(AbstractMBAreaRelation):
    type: AreaSeriesRelationType


class MBSeriesArtistRelation(AbstractMBArtistRelation):
    type: ArtistSeriesRelationType


class MBSeriesEventRelation(AbstractMBEventRelation):
    type: EventSeriesRelationType


class MBSeriesLabelRelation(AbstractMBLabelRelation):
    type: LabelSeriesRelationType


class MBSeriesPlaceRelation(AbstractMBPlaceRelation):
    type: PlaceSeriesRelationType


class MBSeriesRecordingRelation(AbstractMBRecordingRelation):
    type: RecordingSeriesRelationType


class MBSeriesReleaseRelation(AbstractMBReleaseRelation):
    type: ReleaseSeriesRelationType


class MBSeriesReleaseGroupRelation(AbstractMBReleaseGroupRelation):
    type: ReleaseGroupSeriesRelationType


class MBSeriesSeriesRelation(AbstractMBSeriesRelation):
    type: Literal["subseries", "award ceremony", "recorded during", "named after series"]


class MBSeriesUrlRelation(AbstractMBUrlRelation):
    type: SeriesUrlRelationType


class MBSeriesWorkRelation(AbstractMBWorkRelation):
    type: SeriesWorkRelationType


class MBWorkAreaRelation(AbstractMBAreaRelation):
    type: AreaWorkRelationType


class MBWorkArtistRelation(AbstractMBArtistRelation):
    type: ArtistWorkRelationType


class MBWorkEventRelation(AbstractMBEventRelation):
    type: EventWorkRelationType


class MBWorkLabelRelation(AbstractMBLabelRelation):
    type: LabelWorkRelationType


class MBWorkPlaceRelation(AbstractMBPlaceRelation):
    type: PlaceWorkRelationType


class MBWorkRecordingRelation(AbstractMBRecordingRelation):
    type: RecordingWorkRelationType


class MBWorkReleaseGroupRelation(AbstractMBReleaseGroupRelation):
    type: ReleaseGroupWorkRelationType


class MBWorkSeriesRelation(AbstractMBSeriesRelation):
    type: SeriesWorkRelationType


class MBWorkUrlRelation(AbstractMBUrlRelation):
    type: UrlWorkRelationType


class MBWorkWorkRelation(AbstractMBWorkRelation):
    type: Literal[
        "adaptation",
        "arrangement",
        "based on",
        "included works",
        "lyrical quotation",
        "medley",
        "musical quotation",
        "named after work",
        "orchestration",
        "other version",
        "parts",
        "revision of",
    ]
