# anti_pattern_migracao.py — apenas para leitura, nao executar
# Estado preso a memoria da instancia: sessao perdida ao migrar

session_store = {}  # dicionario em memoria local

def save_session(user_id: str, data: dict):
    session_store[user_id] = data   # existe apenas NESTE processo

def get_session(user_id: str) -> dict:
    return session_store.get(user_id, {})

save_session("user_42", {"cart": ["item_1"]})
# Se este processo for encerrado e outro assumir o trafego,
# session_store estara vazio na nova instancia.
print(get_session("user_42"))   # ok aqui
# [processo encerrado — nova instancia sobe em outro servidor]
print(get_session("user_42"))   # {} — sessao perdida!