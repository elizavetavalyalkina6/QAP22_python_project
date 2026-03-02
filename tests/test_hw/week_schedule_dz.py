import pytest
import week_schedule


@pytest.mark.parametrize(
    "num, zon, res",
    [
        (
            3,
            "Europe/Helsinki",
            [("Mo", "02/03", "00:05–22:55"), ("Tu", "03/03", "00:05–22:55"), ("We", "04/03", "00:05–22:55")],
        ),
        (
            4,
            "Europe/Helsinki",
            [
                ("Mo", "02/03", "00:05–22:55"),
                ("Tu", "03/03", "00:05–22:55"),
                ("We", "04/03", "00:05–22:55"),
                ("Th", "05/03", "00:05–22:55"),
            ],
        ),
        (0, "Europe/Helsinki", []),
        (-1, "Europe/Helsinki", []),
        (2, "Europe/Minsk", [("Mo", "02/03", "00:05–22:55"), ("Tu", "03/03", "00:05–22:55")]),
        (
            3,
            "Europe/Minsk",
            [("Mo", "02/03", "00:05–22:55"), ("Tu", "03/03", "00:05–22:55"), ("We", "04/03", "00:05–22:55")],
        ),
        (2, "America/Los_Angeles", [("Mo", "02/03", "00:05–22:55"), ("Tu", "03/03", "00:05–22:55")]),
    ],
)
def test_week_schedule(num, zon, res):
    assert week_schedule.generate_week_schedule(num, zon) == res
