from __future__ import annotations

from datetime import datetime, timedelta, timezone

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
