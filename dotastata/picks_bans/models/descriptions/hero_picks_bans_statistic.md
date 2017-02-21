# hero_picks_bans_700_statistic
Таблица с пиками-банами определенного героя с агрегацией за сутки.

Заполняется кроном на основании данных opendota.

### Скрипт создания
```sql
CREATE TABLE "hero_picks_bans_700_statistic" (
	"id" serial NOT NULL,
	"hero_id" smallint NOT NULL,
	"date" DATE NOT NULL,
	"first_stage_picked" json NOT NULL,
	"first_stage_banned" smallint NOT NULL,
	"second_stage_banned" smallint NOT NULL,
	"second_stage_picked" smallint NOT NULL,
	"third_stage_picked" smallint NOT NULL,
	"third_stage_banned" smallint NOT NULL,
	CONSTRAINT hero_picks_bans_700_statistic_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

```

### Пояснение полей
Название | Тип | Описание
---------|-----|---------
id | bigserial | просто айдишник записи
hero_id | bigint | айдишник героя (fk к таблице hero)
date | date | дата, за которую собрана статистика
N_stage_picked | json | какими командами, в каких матчах, кем и на какую позицию был пикнут текущий герой в стадии N пиков
N_stage_banned | json | какими командами, в каких матчах был забанен текущий герой в стадии N банов

json-поля пиков имеют следующую структуру:
```json
[
    {
        team_id : 1,
        matches : [
            {
                match_id: 11,
                player_id: 111,
                position_id: 2,
            },
            ...
        ]
    },
    ...
]
```

json-поля банов имеют следующую структуру:
```json
[
    {
        team_id : 1,
        match_id : 2
    },
    ...
]
```