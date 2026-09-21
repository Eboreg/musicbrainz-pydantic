# musicbrainz-pydantic

<img width="400" alt="thisprojectwascodedbyahumanbeing-wordart" src="https://github.com/user-attachments/assets/2e36f279-91d9-4f65-9c8f-fd8e6b179f7a" />

[Pydantic](https://pydantic.dev/docs/validation/latest/get-started/) models for the [Musicbrainz API](https://musicbrainz.org/doc/MusicBrainz_API).

Caveat: I have done rather extensive manual testing, but the Musicbrainz API is pretty hairy, and sometimes the documentation is lacking or flat out wrong. So in a few cases (like `MBWork.attributes`) the implementation is based on trial-and-error and a little bit of guesswork.
