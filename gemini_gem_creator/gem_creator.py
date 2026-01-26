import sys
import json
import os

def load_examples():
    """Carica gli esempi dal file JSON."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "examples.json")
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return []

def find_relevant_example(task_input, examples):
    """Trova l'esempio più pertinente in base alle parole chiave."""
    task_input = task_input.lower()
    for example in examples:
        if any(keyword in task_input for keyword in example.get("keywords", [])):
            return example
    return None

def generate_gem_instructions(persona, task, context, format_output):
    """Genera un blocco di istruzioni formattato per un Gemini Gem."""
    instructions = f"""# Istruzioni del Gem

## 🎭 Persona
{persona}

## 📋 Attività (Task)
{task}

## 🌐 Contesto
{context}

## 📄 Formato dell'Output
{format_output}

---
**Nota per l'utente**: Ricorda di testare queste istruzioni nell'anteprima e di fare clic su **Salva** (l'anteprima non salva automaticamente).
"""
    return instructions

def main():
    print("--- 💎 Gemini Gem Creator 💎 ---")
    print("Guida alla creazione di istruzioni ottimizzate.\n")

    examples = load_examples()

    persona = input("1. Persona (Qual è il ruolo e il tono del Gem?): ")
    task = input("2. Attività (Cosa deve fare o creare il Gem?): ")

    # Suggerimento basato sull'esempio
    relevant = find_relevant_example(task, examples)
    if relevant:
        print(f"\n💡 [SUGGERIMENTO] Basato sulla tua attività, ecco un esempio di contesto e formato ({relevant['name']}):")
        print(f"   - Contesto suggerito: {relevant['context']}")
        print(f"   - Formato suggerito: {relevant['format']}\n")

    context = input("3. Contesto (Quali informazioni di background sono necessarie?): ")
    format_output = input("4. Formato (Qual è la struttura dell'output desiderata?): ")

    result = generate_gem_instructions(persona, task, context, format_output)

    print("\n--- ISTRUZIONI GENERATE ---")
    print(result)
    print("---------------------------\n")

    power_up = input("Vuoi generare un prompt di 'Power Up' per espandere queste istruzioni con Gemini? (s/n): ")
    if power_up.lower() == 's':
        print("\nCopia e incolla questo prompt in Gemini per espandere le istruzioni:")
        print(f"\"Riscrivi ed espandi queste istruzioni per un Gemini Gem mantenendo i 4 pilastri (Persona, Task, Context, Format) ma aggiungendo dettagli per renderlo più efficace:\nPersona: {persona}\nTask: {task}\nContext: {context}\nFormat: {format_output}\"")

if __name__ == "__main__":
    main()
