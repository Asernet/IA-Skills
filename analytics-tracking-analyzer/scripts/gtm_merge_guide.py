import json
import os
import argparse
import sys

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Errore nel caricamento del file {path}: {e}")
        return None

def extract_container_data(data):
    """Estrae Tags, Triggers e Variables dal JSON Export di GTM."""
    container = data.get('containerVersion', {}).get('container', {}) if 'containerVersion' in data else data.get('container', {})
    
    # GTM Export structure usually has tag, trigger, variable lists inside 'containerVersion'
    wrapper = data.get('containerVersion', data)
    
    tags = {t['name']: t for t in wrapper.get('tag', [])}
    triggers = {t['name']: t for t in wrapper.get('trigger', [])}
    variables = {t['name']: t for t in wrapper.get('variable', [])}
    
    return tags, triggers, variables

def format_tag_instruction(tag, triggers_map):
    """Formatta le istruzioni per creare un tag."""
    firing_triggers = tag.get('firingTriggerId', [])
    blocking_triggers = tag.get('blockingTriggerId', [])
    
    trigger_names = []
    # Nota: Gli ID nel JSON export spesso riferiscono a ID numerici interni, ma per una guida umana servono i nomi.
    # Tuttavia, il JSON export standalone potrebbe non avere la mappatura facile se non si incrociano gli ID.
    # In questa versione semplificata, elenchiamo le proprietà chiave.
    
    params = tag.get('parameter', [])
    param_str = "\n".join([f"    - **{p['key']}**: {p['value']}" for p in params if 'value' in p])
    
    return f"""
### 🏷️ Tag: {tag['name']}
- **Tipo**: `{tag['type']}`
- **Configurazione**:
{param_str}
- **Trigger di Attivazione**: *(Verifica corrispondenza ID/Nome nel JSON)*
- **Note**: Assicurati di impostare il Consent Settings se 'Compliance' è attiva.
"""

def generate_guide(new_data, old_data=None, output_path="GUIDA_INTEGRAZIONE_GTM.md"):
    print("Analisi delle configurazioni in corso...")
    
    new_tags, new_triggers, new_vars = extract_container_data(new_data)
    
    items_to_create = {
        'tags': [],
        'triggers': [],
        'variables': []
    }
    
    if old_data:
        old_tags, old_triggers, old_vars = extract_container_data(old_data)
        
        # Semplice diff per nome
        for name, tag in new_tags.items():
            if name not in old_tags:
                items_to_create['tags'].append(tag)
            else:
                pass # Esiste già, per ora ignoriamo (assumiamo che l'esistente vinca o richieda audit manuale)
                
        for name, trig in new_triggers.items():
            if name not in old_triggers:
                items_to_create['triggers'].append(trig)

        for name, var in new_vars.items():
            if name not in old_vars:
                items_to_create['variables'].append(var)
                
        intro_text = f"## 📊 Report di Integrazione\nBasato sul confronto col GTM attuale.\nElementi mancanti da aggiungere manualmente:"
    else:
        # Tutto è nuovo
        items_to_create['tags'] = list(new_tags.values())
        items_to_create['triggers'] = list(new_triggers.values())
        items_to_create['variables'] = list(new_vars.values())
        intro_text = "## 🚀 Guida all'Installazione Completa\nSegui questi step per configurare il container da zero o integrare manualmente."

    # Scrittura MD
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Guida Integrazione GTM\n\n{intro_text}\n\n")
        
        if items_to_create['variables']:
            f.write("## 1. Variabili\nCrea queste variabili prima dei trigger/tag.\n")
            for v in items_to_create['variables']:
                f.write(f"- **{v['name']}** ({v['type']})\n")
            f.write("\n---\n")
            
        if items_to_create['triggers']:
            f.write("## 2. Trigger\nConfigura i seguenti attivatori:\n")
            for t in items_to_create['triggers']:
                f.write(f"### ⚡ {t['name']}\n- **Tipo**: {t['type']}\n")
                # Add filters logic here if needed
            f.write("\n---\n")
            
        if items_to_create['tags']:
            f.write("## 3. Tag\nInfine, crea i tag collegandoli ai trigger creati:\n")
            for t in items_to_create['tags']:
                f.write(format_tag_instruction(t, {}))
                
    print(f"✅ Guida generata con successo: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="GTM Integration Guide Generator")
    parser.add_argument("proposal_path", help="Percorso del JSON GTM proposto (Compliance)")
    parser.add_argument("--current", help="Percorso del JSON GTM attuale (opzionale)", default=None)
    args = parser.parse_args()
    
    if not os.path.exists(args.proposal_path):
        print(f"Errore: File proposto non trovato: {args.proposal_path}")
        return

    prop_json = load_json(args.proposal_path)
    if not prop_json: return

    current_path = args.current
    
    # Se non fornito via arg, chiedi solo se siamo in sessione interattiva (ma l'agente chiamerà con arg se l'utente lo da)
    # Per semplicità, se l'Agente lo usa, si aspetta che passi l'arg o nulla.
    # Se l'utente lo lancia a mano senza arg, chiediamo.
    if not current_path and sys.stdin.isatty():
        print("\n" + "="*50)
        print(" 🛠️  G WIZARD INTEGRATION ASSISTANT")
        print("="*50)
        print("Il sistema ha generato una configurazione 'Ideal Compliance'.")
        print("Vuoi confrontarla con il tuo GTM attuale per generare una guida passo-passo differenziale?")
        
        current_path = input("\nInserisci il percorso assoluto del tuo export GTM attuale (o premi INVIO per generare la guida completa): ").strip().strip('"').strip("'")
    
    old_json = None
    if current_path:
        if os.path.exists(current_path):
            print(f"Caricamento GTM attuale: {current_path}...")
            old_json = load_json(current_path)
        else:
            print(f"⚠️  File {current_path} non trovato. Procedo con la guida completa.")
            
    output_dir = os.path.dirname(args.proposal_path)
    output_file = os.path.join(output_dir, "GUIDA_INTEGRAZIONE_GTM.md")
    
    generate_guide(prop_json, old_json, output_file)

if __name__ == "__main__":
    main()
