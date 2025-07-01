# Instagram Yuklab Olish Bot (Telegram uchun) 📥

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/badge/contributors-1-lightgrey)

Instagram postlari, reels (video) va profil rasmlarini Telegram orqali bevosita yuklab olish imkonini beruvchi kuchli funksiyalarga ega Telegram boti. Python yordamida yaratilgan va Instaloader + Telethon texnologiyalarida ishlaydi.

## Asosiy imkoniyatlar

- Instagram postlari va reels videolarini yuklab olish (video va rasm)
- Instagram profil rasmini va biografiyasini ko‘rish
- Admin panel: foydalanuvchilar statistikasi
- Barcha foydalanuvchilarga xabar yuborish (broadcast)
- Xatoliklar uchun log yuritish tizimi
- Redis ma'lumotlar bazasi bilan integratsiya

## O‘rnatish

1. Repozitoriyani klonlang:
   ```bash
   git clone https://github.com/FAZOVFX/instagramdownloaderbot.git
   cd instagramdownloaderbot
   ```

2. Kerakli kutubxonalarni o‘rnating:
   ```bash
   pip install -r requirements.txt
   ```

## Sozlash

Loyihaning asosiy papkasida `.env` fayl yarating va quyidagilarni yozing:

```env
API_ID=telegram_api_id
API_HASH=telegram_api_hash
BOT_TOKEN=telegram_bot_token
AUTH_USER_ID=admin_telegram_id
REDIS_HOST=redis_host
REDIS_PORT=redis_port
REDIS_PASSWORD=redis_password
```

## Foydalanish

1. Botni ishga tushiring:
   ```bash
   python main.py
   ```

2. Instagram linklarini botga yuboring:
   - Post: `https://www.instagram.com/p/abc123`
   - Reels: `https://www.instagram.com/reel/xyz456`
   - Profil: `https://www.instagram.com/username/`

Bot sizga rasm/video yuboradi. Agar video bo‘lsa, u undagi musiqa (soundtrack)ni aniqlab, ACRCloud orqali qo‘shiq nomi, artisti va YouTube variantlarini ham ko‘rsatadi.

## Buyruqlar

| Buyruq      | Tavsifi                             | Kim uchun         |
|-------------|--------------------------------------|-------------------|
| `/start`    | Botni ishga tushirish                | Barcha foydalanuvchilar |
| `/users`    | Umumiy foydalanuvchilar soni         | Faqat admin       |
| `/bcast`    | Barcha foydalanuvchilarga xabar yuborish | Faqat admin   |
| `/logs`     | Bot xatolik loglarini ko‘rish        | Faqat admin       |

## Redis sozlamalari

- Ma'lumotlar doimiy saqlanmasligi uchun Redis ishlatiladi.
- `Upstash`, `Redis Cloud` yoki o‘z serveringizdan foydalanishingiz mumkin.

## Litsenziya

Ushbu loyiha MIT litsenziyasi ostida tarqatiladi — istalgan maqsadda erkin foydalanishingiz mumkin, ammo mualliflik saqlanishi kerak.

---

📌 GitHub sahifa:  
[https://github.com/FAZOVFX/instagramdownloaderbot](https://github.com/FAZOVFX/instagramdownloaderbot)
