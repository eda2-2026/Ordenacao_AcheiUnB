from datetime import datetime

from .match_ranking import rank_match_candidates


def main() -> None:
    target_item = {
        "id": 1,
        "name": "Fone bluetooth preto",
        "description": "Fone sem fio com estojo oval e borrachas pequenas.",
        "color": "Preto",
        "brand": "JBL",
        "found_lost_date": datetime(2026, 4, 10, 10, 0),
    }

    # Estes candidatos representam itens que já passaram pela filtragem inicial por status, categoria e local.
    candidates = [
        {
            "id": 2,
            "name": "Headphone bluetooth preto",
            "description": "Fone de arco acolchoado com hastes grandes.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 14, 10, 0),
        },
        {
            "id": 3,
            "name": "Estojo de fone preto",
            "description": "Fone com estojo oval preto e borrachas pequenas.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 10, 10, 0),
        },
        {
            "id": 4,
            "name": "Fone preto sem fio",
            "description": "Fone sem fio com estojo oval e borrachas pequenas.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 12, 10, 0),
        },
        {
            "id": 5,
            "name": "Fone bluetooth preto",
            "description": "Fone sem fio com estojo oval e borrachas pequenas.",
            "color": "Preto",
            "brand": "JBL",
            "found_lost_date": datetime(2026, 4, 11, 10, 0),
        },
        {
            "id": 6,
            "name": "Carregador de notebook",
            "description": "Carregador com cabo grosso e conector redondo.",
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

    print(f"\nTotal de candidatos antes do ranqueamento: {len(candidates)}")
    print(f"Total de candidatos após o score mínimo: {len(ranked_matches)}")


if __name__ == "__main__":
    main()