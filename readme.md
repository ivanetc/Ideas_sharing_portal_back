# Ссылка на второй репозиторий (frontend) - https://github.com/interhub/webapp

# API
## User
### /user/get_user
return
```json
    {
        "result": true, 
        "data": {
                  "user_id": 1, 
                  "first_name": "Алекандр", 
                  "second_name": "Сергеевич", 
                  "last_name": "Иванец", 
                  "image": "картинка", 
                  "city": "Ярославль", 
                  "department": "Управление трехмерного моделирование", 
                  "position": ".net разработчик", 
                  "office_phone": "89052668317", 
                  "email": "ivanetcas@polymetal.ru", 
                  "achievements": [
                        {
                          "id": 1, 
                          "name": "Первопроходец", 
                          "description": "Поздравляю, теперь ты первопроходец! С освоением ключевого функционала портала!", 
                          "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhE"
                        }
                  ]
        }
}
```

### /idea/get_group_by_tag
в body {tag: "tagName}"
return
```json
    {
      "result": true, 
      "data": [
          {
            'group_id': 1, 
            'group_title': 'Группа первая', 
            'ideas': [
                {
                   'name': 'Социальная сеть инвестора', 
                   'id': 1, 
                   'author_id': 1, 
                   'text': 'Предлагаю добавить в наше мобильное приложение раздел, где пользователи могут общаться, обмениваться сообщениями по инвестициям. Некоторая социальная сеть для инвесторов', 
                   'tags': ['cоциальная сеть', 'общение']
                }
              ]
            }
        ]
          
    }
```

### /tag/get_tags_rating
return
```json
    {
      "result": true, 
      "tags": [{"name": "общение", "rating": 4}]
    }
```

### /user/get_users_rating
return
```json
    {
      "result": true, 
      "users": [{"name": "Александр", "id": 1, "rating": 3}]
    }
```

### /user/get_top_groups
return
```json
    {
      "result": true, 
      "groups": [{"name": "Группа 1", "id": 1, "rating": 232}]
    }
```

### idea/get_top_ideas
```json
{
  "result": true, 
  "data": 
    [
      {
        "name": "Больше зеркал у ксерокса", 
        "id": 2, 
        "author_id": 2, 
        "text": "Мне кажется у ксерокса не хватает зеркал. Нужно их установить, они позволят смотреть на себя пока идет печать и позволят оценивать обстановку со всех сторон)", 
        "tags": [], 
        "rating": 100500
      }
    ]
} 
```

### /idea/add_idea_to_group
send
```json
{
  "group_id": 1,
  "name": "Название идеи",
  "text": "Я хочу пожрать",
  "author_id": 2,
  "tags": ["еда"]
}
```

### /idea/add_new_group
send
```json
{
  "group_name": "Мы все хотим пожрать",
  "name": "Название идеи",
  "text": "Я хочу пожрать",
  "author_id": 2,
  "tags": ["еда"]
} 
```
### /user/get_relevant_ideas
return
```json
    {
      "result": true, 
      "groups": [
        {
          "name": "Группа 1",
          "id": 1,
          "rel_text": "Текст наиболее релевантной идеи из этой группы",
          "ideas": [
            {
              "name": "Название идеи",
              "id": 1,
              "author_id": 7,
              "text": "Текст идеи",
              "tags": ["музыка"],
              "rating": 22
            }
          ]
        }
      ],
      "tags": ["текст", "идея"]
    }
```
