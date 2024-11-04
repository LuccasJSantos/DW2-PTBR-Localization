import ollama

def execute(text: str, context: str = ''):
    return ollama.chat(model = 'mistral-nemo', messages = [
        { 'role': 'system', 'content': 'Your are a professional English to Brazilian Portuguese translator specialized in the sci-fi genre.' },
        { 'role': 'system', 'content': 'Your translation must respect the sci-fi theme.' },
        { 'role': 'system', 'content': 'You dont need to explain why you translated the way you did, no need to add your AI translation notes.' },
        { 'role': 'system', 'content': 'Beware of tags in brackets or braces, keep them intact' },
        { 'role': 'system', 'content': 'Return the response without formatting it with bold, list, etc' },
        { 'role': 'system', 'content': context },
        { 'role': 'user', 'content': f"Text to translate: {text}" },
    ])


def translate(source_path: str, target_path: str):
    print(f'Translate: {source_path}')
    file = open(source_path, 'r', encoding='windows-1252')

    file_content_response = execute(file.read())

    translated_file = open(target_path, 'w', encoding='utf-8')
    translated_file.write(file_content_response['message']['content'])
    translated_file.close()
