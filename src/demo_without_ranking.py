from datetime import datetime


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

    print("Possíveis matches sem ranqueamento:\n")
    for position, item in enumerate(candidates, start=1):
        print(f"{position}. {item['name']} | id: {item['id']}")

    print(f"\nTotal de candidatos exibidos: {len(candidates)}")


if __name__ == "__main__":
    main()