from datetime import datetime

from .match_ranking import rank_match_candidates


def main() -> None:
    target_item = {
        "id": 1,
        "name": "Fone bluetooth preto",
        "description": "Fone sem fio preto perdido próximo à biblioteca.",
        "color": "Preto",
        "brand": "JBL",
        "found_lost_date": datetime(2026, 4, 10, 10, 0),
    }

    # Estes candidatos representam itens que já passaram pela filtragem inicial por status, categoria e local.
    candidates = [
        {
            "id": 2,
            "name": "Headphone bluetooth preto",
            "description": "Headphone preto encontrado próximo à biblioteca.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 14, 10, 0),
        },
        {
            "id": 3,
            "name": "Estojo de fone preto",
            "description": "Estojo preto da marca JBL encontrado próximo à biblioteca.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 10, 10, 0),
        },
        {
            "id": 4,
            "name": "Fone preto sem fio",
            "description": "Fone bluetooth preto encontrado na biblioteca.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 12, 10, 0),
        },
        {
            "id": 5,
            "name": "Fone bluetooth preto",
            "description": "Fone sem fio preto encontrado próximo à biblioteca.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 11, 10, 0),
        },
        {
            "id": 6,
            "name": "Carregador de notebook",
            "description": "Carregador encontrado em sala de aula.",
            "color": "Branco",
            "brand": "Dell",
            "found_lost_date": datetime(2026, 4, 10, 10, 0),
        },
    ]

    ranked_matches = rank_match_candidates(target_item, candidates)

    print("Ranking de possíveis matches:\n")
    for position, ranked_match in enumerate(ranked_matches, start=1):
        item = ranked_match.item
        print(
            f"{position}. {item['name']} "
            f"| id: {item['id']} "
            f"| score: {ranked_match.score}"
        )


if __name__ == "__main__":
    main()