#!/usr/bin/env python
import os
import random
import re
import json

directory = os.getcwd()
translation_data = {}
keys = set()
# scan .lproj folder
for root, dirs, files in os.walk(directory):
    for directory in dirs:
        if directory.endswith(".lproj"):
            language_code = directory.replace(".lproj", "")
            language_folder = os.path.join(root, directory)

            # find Localizable.strings
            strings_file = os.path.join(language_folder, "Localizable.strings")

            if os.path.exists(strings_file):
                with open(strings_file, "r", encoding="utf-8") as file:
                    language_strings = file.read()

                pattern = r'"(.+)" = "(.+)";'
                string_pairs = re.findall(pattern, language_strings)

                language_dict = {}

                for key, value in string_pairs:
                    language_dict[key] = value
                    keys.add(key)

                translation_data[language_code] = language_dict

# write into .xcstrings file
xcstringsFileData = {
    "sourceLanguage": random.choice(list(translation_data.keys())),
    "strings": {},
    "version": "1.0"
}
stringsDict = {}
for key in keys:
    localizactionsDict = {}

    for lang, translationDict in translation_data.items():
        if key in translationDict:
            localizactionsDict[lang] = {
                "stringUnit": {
                    "state": "translated",
                    "value": translationDict[key]
                }
            }
    stringsValue = {
        "extractionState": "manual",
        "localizations": localizactionsDict
    }
    stringsDict[key] = stringsValue

xcstringsFileData["strings"] = stringsDict

output_file = os.path.join(directory, "Localizable.xcstrings")

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(xcstringsFileData, json_file, ensure_ascii=False, indent=2)

print(f"Localization data has been extracted and saved to {output_file}")
