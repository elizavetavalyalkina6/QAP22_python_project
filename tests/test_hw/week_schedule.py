from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def generate_week_schedule(days_ahead: int = 7, tz: str = "Europe/Helsinki") -> list[tuple[str, str, str]]:
    """
    Генерирует расписание на несколько дней вперёд с учётом часового пояса.

    Для каждого дня формируется кортеж из трёх элементов:
    - сокращённое название дня недели (Mo, Tu, We, Th, Fr, Sa, Su);
    - дата в формате DD/MM;
    - строка с временем работы или значением "Closed" для выходных.

    Логика работы:
    - отсчёт начинается с текущей даты в указанном часовом поясе;
    - для будних дней (понедельник–пятница) время работы фиксировано:
      "00:05–22:55";
    - для выходных (суббота и воскресенье) возвращается "Closed";
    - количество дней определяется параметром `days_ahead`.

    Примеры:
        >>> generate_week_schedule(3, tz="Europe/Helsinki")
        [('Mo', '01/01', '00:05–22:55'),
         ('Tu', '02/01', '00:05–22:55'),
         ('We', '03/01', '00:05–22:55')]

        >>> generate_week_schedule(2, tz="Europe/Helsinki")
        [('Sa', '06/01', 'Closed'),
         ('Su', '07/01', 'Closed')]

    :param days_ahead: Количество дней вперёд, для которых нужно сгенерировать
                       расписание (по умолчанию 7).
    :param tz: Часовой пояс в формате IANA (например, "Europe/Helsinki").
    :return: Список кортежей вида (день_недели, дата, время_работы).
    """
    day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    today = datetime.now(ZoneInfo(tz)).date()
    lst = []
    for i in range(days_ahead):
        d = today + timedelta(days=i)
        wd = d.weekday()  # 0..6
        day_abbr = day_names[wd]
        date_str = d.strftime("%d/%m")
        time_str = "Closed" if wd >= 5 else "00:05–22:55"
        lst.append((day_abbr, date_str, time_str))
    return lst
