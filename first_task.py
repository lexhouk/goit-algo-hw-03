from datetime import datetime, date as date_only


def get_days_from_today(date: str) -> int:
    '''
    Calculate the number of days between the current date and the specified
    date.

    :param date: string

    :return: integer
    '''
    
    try:
        given: datetime = datetime.strptime(date, '%Y-%m-%d')
    except Exception:
        print('The "date" argument must match this pattern: "YYYY-MM-DD"!')
        return None
    
    return (date_only.today() - given.date()).days
