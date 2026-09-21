import shelve
from datetime import datetime
from typing import Any

from pydantic import Field

from musicbrainz_pydantic import APP_DIRS
from musicbrainz_pydantic.models.base import AbstractBaseMBModel


class ShelfEntry(AbstractBaseMBModel):
    id: str
    inc: list[str]
    entity_json: dict[str, Any]
    created: datetime = Field(default_factory=datetime.now)


def get_from_shelf(entity_type: str, id: str, inc: list[str]) -> dict[str, Any] | None:
    with shelve.open(APP_DIRS.user_data_path / "musicbrainz.db") as shelf:
        for entry_json in shelf.get(entity_type, []):
            entry = ShelfEntry.model_validate_json(entry_json)
            if entry.id == id and all(i in entry.inc for i in inc):
                return entry.entity_json
    return None


def save_to_shelf(entity_type: str, id: str, inc: list[str], entity_json: dict[str, Any]):
    with shelve.open(APP_DIRS.user_data_path / "musicbrainz.db") as shelf:
        better_entry_exists = False
        entry_list: list[ShelfEntry] = []

        for entry_json in shelf.get(entity_type, []):
            entry = ShelfEntry.model_validate_json(entry_json)
            if entry.id != id or not all(i in inc for i in entry.inc):
                if entry.id == id and all(i in entry.inc for i in inc) and len(entry.inc) > len(inc):
                    better_entry_exists = True
                entry_list.append(entry)

        if not better_entry_exists:
            entry_list.append(ShelfEntry(inc=inc, entity_json=entity_json, id=id))
        shelf[entity_type] = [entry.model_dump_json() for entry in entry_list]
