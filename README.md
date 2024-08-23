
# FastAPI Temaplte

## Qamrab oladi:

- User Modellar
- Authentication | Authorization
- Unittestlar
- JWT
- PostgresSQL(SQLAlchemy|Alembic)
- Email Validation

## Avzalliklari
- Foydalanish uchun qulay
- Tushunishga oson
- Ko'p qamrovli


## Foydalanish uchun:

1. Kerakli papkaga boring va kodni githubdan yuklab oling.
```bash
$ git clone https://github.com/Abdurasuloff/fastapi-template.git
```

2. Vertual muhit yaratib uni ichiga kiring va kerakli kutubxonalarni o'rnating,
```bash
$ pip install -r requirements.txt 
```
3. .env faylini .env.example fayliga qarab kerakli ma'lumotlar bilan to'ldiring
4. Serverni ishga tushuring:

```bash
$ uvicorn app.main:app --reload
```

## Testlarni ishga tushurish.
1. .env testlar uchun boshqa databaseni ko'rsatgan bo'lishingiz kerak.
2. Test databaseni sozlash uchun:
```bash
$ python setup.py
```
3. Testlarni ishga tushuring
```bash
$ pytest
```

## Eslatma
Kodlar menga tegishli emas. Lekin bularni o'zgaritishimiz mumkin. Ushbu template uchun takliflar bo'lsa bemalol aloqaga chiqing.

Credit | Asl nusxa: https://github.com/seapagan/fastapi-template.git

(Kimdir manga README yozib bersin)