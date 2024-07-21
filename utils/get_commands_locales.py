import json
from utils.languages import text, get_languages_info


def get_commands_locales() -> dict:
    """
    Load and process command localization data from a JSON file.

    This function reads the 'config/commands.json' file, which contains localization
    information for bot commands. It processes this data to create a structured
    dictionary of command locales, including translations for command names,
    descriptions, and arguments across multiple languages.

    Returns:
        dict: A dictionary containing localized information for each command.
              The structure is:
              {
                  'command_name': {
                      'name': {lang_code: localized_name, ...},
                      'desc': {lang_code: localized_description, ...},
                      'args': [
                          {
                              'name': {lang_code: localized_arg_name, ...},
                              'desc': {lang_code: localized_arg_description, ...},
                              ...
                          },
                          ...
                      ]
                  },
                  ...
              }

    Note:
        - The function uses the 'get_languages_info()' function to obtain supported language codes.
        - It processes both string and dictionary type localizations.
        - For command names, it applies lowercase transformation to maintain consistency.
    """

    lang_codes = [lang["code"] for lang in get_languages_info()]
    print('Available langs:', lang_codes)
    
    with open('config/commands.json', 'r', encoding='utf-8') as commands_file:
        commands = json.load(commands_file)
    
    commands_locales = {}
    for category, category_commands in commands['categories'].items():
        for command_name, command_data in category_commands.items():
            
            commands_locales[command_name] = command_data.copy()
            
            for param in ['name', 'desc']:
                if isinstance(command_data.get(param), dict):
                    commands_locales[command_name][param] = command_data[param]
                elif isinstance(command_data.get(param), str):
                    commands_locales[command_name][param] = {}
                    for lang in lang_codes:
                        commands_locales[command_name][param][lang] = text(command_data[param], lang)
            
            if isinstance(command_data.get('args'), list):
                commands_locales[command_name]['args'] = command_data['args']
                for arg in commands_locales[command_name]['args']:
                    if isinstance(arg, dict):
                        for param in ['name', 'desc']:
                            if arg.get(param):
                                if isinstance(arg.get(param), str):
                                    arg[param] = {
                                        lang: text(arg[param], lang)
                                        for lang in lang_codes
                                    }
    
    return commands_locales