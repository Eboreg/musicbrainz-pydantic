from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol

from pydantic import Field

from musicbrainz_pydantic.models.base import AbstractBaseMBModel
from musicbrainz_pydantic.utils import YearOrNone


if TYPE_CHECKING:
    from musicbrainz_pydantic.models.core import MBArtist, MBLabel, MBRecording


class DiscTOCProto(Protocol):
    offsets: list[int]
    sectors: int
    track_count: int

    def get_track_lengths_ms(self) -> list[int]: ...


class MBAlias(AbstractBaseMBModel):
    begin: Any = None
    end: Any = None
    ended: bool | None = None
    locale: str | None = None
    name: str
    primary: bool | None = None
    sort_name: str
    type_id: str | None = None
    type: str | None = None


class MBArtistCredit(AbstractBaseMBModel):
    joinphrase: str | None = None
    name: str

    artist: MBArtist


class MBAttribute(AbstractBaseMBModel):
    value: str
    type_id: str
    type: str


class MBDisc(AbstractBaseMBModel):
    id: str
    sectors: int
    offset_count: int

    offsets: list[int]

    def get_rank(self, toc: DiscTOCProto) -> int:
        track_count_diff = abs(self.offset_count - toc.track_count)
        offsets_diff = sum(abs(o1 - o2) for o1, o2 in zip(self.offsets, toc.offsets, strict=False))
        return (track_count_diff * 100_000) + offsets_diff

    def matches_toc(self, toc: DiscTOCProto):
        return self.sectors == toc.sectors and self.offset_count == toc.track_count and self.offsets == toc.offsets


class MBLabelInfo(AbstractBaseMBModel):
    catalog_number: str | None = None

    label: MBLabel | None = None


class MBLifeSpan(AbstractBaseMBModel):
    begin: str | None = None
    end: str | None = None
    ended: bool | None = None


class MBMedium(AbstractBaseMBModel):
    format: str | None = None
    id: str
    position: int = 1
    title: str | None = None
    track_count: int

    discs: list[MBDisc] = Field(default_factory=list)
    tracks: list[MBTrack] = Field(default_factory=list)

    def get_disc_id_by_toc(self, toc: DiscTOCProto):
        for disc in self.discs:
            if disc.matches_toc(toc):
                return disc.id
        return None

    def get_rank(self, track_lengths: list[int]) -> int:
        track_count_diff = abs(len(self.tracks) - len(track_lengths))
        # Milliseconds:
        own_lengths = [t.length or (t.recording.length if t.recording else 0) or 0 for t in self.tracks]
        lengths_diff = sum(abs(l1 - l2) for l1, l2 in zip(track_lengths, own_lengths, strict=False))
        return (track_count_diff * 100_000) + lengths_diff

    def get_rank_by_toc(self, toc: DiscTOCProto) -> int:
        if self.discs:
            return min(disc.get_rank(toc) for disc in self.discs)
        return self.get_rank(toc.get_track_lengths_ms())


class MBRating(AbstractBaseMBModel):
    votes_count: int
    value: float | None = None


class MBReleaseEvent(AbstractBaseMBModel):
    date: YearOrNone = None


class MBTag(AbstractBaseMBModel):
    count: int
    name: str


class MBTextRepresentation(AbstractBaseMBModel):
    language: str | None = None
    script: str | None = None


class MBTrack(AbstractBaseMBModel):
    id: str
    length: int | None = None
    number: str
    position: int
    title: str

    recording: MBRecording | None = None

    artist_credit: list[MBArtistCredit] = Field(default_factory=list)

    def artist(self) -> str:
        artist = ""
        for ac in self.get_artist_credit():
            if ac.joinphrase:
                artist += f"{ac.name}{ac.joinphrase}"
            else:
                artist += ac.name
        return artist

    def get_artist_credit(self) -> list[MBArtistCredit]:
        return self.recording.artist_credit if self.recording and self.recording.artist_credit else self.artist_credit
