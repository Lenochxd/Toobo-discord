import os

lang_files = {}
languages_info = []


def load_lang_file(lang: str) -> dict:
    lang_dictionary = {}
    lang_path = f"texts/{lang}.lang"
    if not os.path.isfile(f"texts/{lang}.lang"):
        for root, dirs, files in os.walk("texts"):
            for file in files:
                if file.endswith(".lang") and file.startswith(lang):
                    lang_path = f"texts/{file}"

    with open(lang_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if (
                line.replace(" ", "").replace("\n", "") != ""
                and not line.startswith("//")
                and not line.startswith("#")
            ):
                try:
                    key, value = line.strip().replace("\n", "").split("=", 1)
                    lang_dictionary[key] = value.strip()
                except Exception as e:
                    line = line.replace("\n", "")
                    print(f'\nLANG FILE ERROR:\nLine: {line}\nError: {e}\n')
    return lang_dictionary

def language_exists(lang: str='en') -> bool:
    lang = next((l for l in lang_files if l.lower().startswith(lang.lower())), 'en')
    return lang in lang_files

def load_all_lang_files() -> dict:
    lang_files = {}
    for root, dirs, files in os.walk("texts"):
        for file in files:
            if file.endswith(".lang"):
                lang = file.split(".")[0]
                lang_files[lang] = load_lang_file(lang)
    return lang_files

def reload_all_lang_files():
    global lang_files
    lang_files = load_all_lang_files()

def get_languages_info(lang_files: dict=lang_files) -> list:
    languages_info = []
    
    if len(lang_files) == 0:
        lang_files = load_all_lang_files()
    
    for lang in lang_files:
        languages_info.append({
            'name': lang,
            'code': lang_files[lang]['lang_code'],
            'native_name': lang_files[lang]['lang_name'],
            'credits': lang_files[lang]['credits'],
        })
        
    return languages_info

def init():
    """
    Initialize language files and information.
    
    This function reloads all language files and retrieves language information.
    
    Returns:
        list: A list of dictionaries containing information about available languages.
    """
    
    global languages_info
    
    reload_all_lang_files()
    
    languages_info = get_languages_info()
    return languages_info

def text(text: str=None, lang: str='en') -> str:
    if text is None:
        return ""
    
    lang = next((l for l in lang_files if l.lower().startswith(lang.lower()[:2])), 'en')
    
    if lang not in lang_files:
        lang = 'en_US'
        
    if text not in lang_files[lang]:
        return text
    
    return lang_files[lang][text].replace(
                     '\\n', '\n').replace(
                     '\\r', '\r')

# Testing
if __name__ == '__main__':
    init()
    while True:
        user_input = input("Enter text to translate (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        print(text(user_input, 'en'))
        