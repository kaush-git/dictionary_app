def parse_dictionary_response(data):
    parsed = {
        "word": "",
        "phonetics": [],
        "meanings": []
    }

    entry = data[0]
    parsed["word"] = entry.get("word", "")

    for phonetic in entry.get("phonetics", []):
        text = phonetic.get("text")
        if text:
            parsed["phonetics"].append(text)

    for meaning in entry.get("meanings", []):
        part_of_speech = meaning.get("partOfSpeech", "")
        definitions = []
        antonyms = []

        for definition in meaning.get("definitions", []):
            definitions.append(definition.get("definition", ""))

            antonyms.extend(definition.get("antonyms", []))

        parsed["meanings"].append({
            "part_of_speech": part_of_speech,
            "definitions": definitions,
            "antonyms": list(set(antonyms))
        })

    return parsed
