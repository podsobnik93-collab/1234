from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Добавляем корень репозитория в путь поиска Python-модулей.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from sportmonks_client import SportmonksClient


def main() -> None:
    today = datetime.now(timezone.utc).date()
    tomorrow = today + timedelta(days=1)

    client = SportmonksClient()

    response = client.get_fixtures_between(
        start_date=today.isoformat(),
        end_date=tomorrow.isoformat(),
    )

    fixtures = response.get("data", [])

    print("Sportmonks connection: OK")
    print(f"Dates: {today} - {tomorrow}")
    print(f"Fixtures received: {len(fixtures)}")

    for fixture in fixtures[:5]:
        print(
            "Fixture:",
            fixture.get("id"),
            fixture.get("name"),
            fixture.get("starting_at"),
        )


if __name__ == "__main__":
    main()
