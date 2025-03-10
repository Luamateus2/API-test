from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_deve_listar_roupa():
    response = client.get('/lojas')
    assert response.status_code == 200

    # Normalizar os preços para float antes de comparar
    resposta_corrigida = [
        {**item, "preco": float(item["preco"])} for item in response.json()
    ]

    assert resposta_corrigida == [
        {'id_roupa': 1, 'nome': "TO", 'tamanho': "M", 'cor': "Azul", 'preco': 34.10},
        {'id_roupa': 2, 'nome': "TOP", 'tamanho': "M", 'cor': "Azul", 'preco': 34.10}
    ]


def test_criar_roupa():
    nova_roupa = {
        "nome": "Topcroped",
        "tamanho": "M",
        "cor": "Azul",
        "preco": 29.90,
    }

    response = client.post("/lojas", json=nova_roupa)
    assert response.status_code == 201

    resposta_json = response.json()

    # Converter preço para float antes de comparar
    resposta_json["preco"] = float(resposta_json["preco"])

    nova_roupa_copy = nova_roupa.copy()
    nova_roupa_copy["id_roupa"] = 3  # Garantir que o ID esteja correto

    assert resposta_json == nova_roupa_copy
