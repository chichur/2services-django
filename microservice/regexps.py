re_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
re_lastname = r"[А-Я][а-я]{1,30}\s[А-Я][а-я]{1,30}\s[А-Я][а-я]{1,30}"
re_company = r"ЗАО\s+[\"«]?[а-яА-Я\s„“]+[\"»]?|" \
             r"ПК\s+[\"«]?[а-яА-Я\s„“]+[\"»]?|" \
             r"ГК\s+[\"«]?[а-яА-Я\s„“]+[\"»]?|" \
             r"ООО\s+[\"«]?[а-яА-Я\s„“]+[\"»]?|" \
             r"ОАО\s+[\"«]?[а-яА-Я\s„“]+[\"»]?|" \
             r"ИП\s+[\"«]?[а-яА-Я\s„“]+[\"»]?|" \
             r"АО\s+[\"«]?[а-яА-Я\s„“]+[\"»]?"
