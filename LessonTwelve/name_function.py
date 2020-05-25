def get_formatted_name(first, last, otch = ''):
    """Возвращает форматированное имя и фамилию, и может быть отчество
    если оно было указано
    """
    if first =='' or last =='':
        return "Введите корректные данные"
    elif otch:
        full_name = f"{first.title().strip()} {last.title().strip()} {otch.title().strip()}"
    else:
        full_name = f"{first.title().strip()} {last.title().strip()}"
    return full_name