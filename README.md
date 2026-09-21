# musicbrainz-pydantic

<img width="500" alt="thisprojectwascodedbyahumanbeing-wordart" src="https://github.com/user-attachments/assets/83071cfd-5aec-4a4d-897d-8aa4a933fa31" />

[Pydantic](https://pydantic.dev/docs/validation/latest/get-started/) models for the [Musicbrainz API](https://musicbrainz.org/doc/MusicBrainz_API).

Caveat: I have done rather extensive manual testing, but the Musicbrainz API is pretty hairy, and sometimes the documentation is lacking or flat out wrong. So in a few cases (like `MBWork.attributes`) the implementation is based on trial-and-error and a little bit of guesswork.
