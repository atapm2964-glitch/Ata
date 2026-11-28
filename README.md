# AtaVision — نسخهٔ ۸۱ (GitHub Pages + Actions + Releases)

محیط آموزشی فیزیک **AtaVision** — نسخهٔ ۸۱. برنامه آفلاین‌اول است؛ GitHub فقط برای
هاست استاتیک (Pages)، ساخت خودکار (Actions) و انتشار (Releases) استفاده می‌شود.
بک‌اند داینامیک (حساب/همگام‌سازی/پنل) روی GitHub وجود ندارد و در این نسخه ساخته نشده است.

## خروجی‌ها

| خروجی | مسیر در مخزن | ساخت |
|---|---|---|
| HTML مستقل | `web/AtaVision-81.0.0.0-Offline.html` | کپی مستقیم؛ روی Pages هم منتشر می‌شود |
| Android APK | `android/` | GitHub Actions (`build-all.yml`) |
| Windows EXE پرتابل x64 | `windows/` | GitHub Actions |
| Windows EXE نصب‌کننده x64 | `windows/` | GitHub Actions (Inno Setup) |

## شناسه‌ها (سازگار با نسخهٔ ۸۰)

- Android applicationId: `ir.fizikland.atavision.ios27v905` (بدون تغییر)
- Android versionCode نسخهٔ ۸۱: `81000000` (بالاتر از `80000000` نسخهٔ ۸۰)
- Android AssetLoader origin: `https://appassets.androidplatform.net/assets/index.html`
- Windows WebView2 origin: `https://appassets.atavision.test/assets/index.html`
- Windows UserData: `%LOCALAPPDATA%\AtaVision\WindowsDesktop\UserData`

## اشتراک نسخهٔ ۸۱

- کدهای نسخهٔ ۸۰ در ۸۱ **معتبر نیستند**؛ برای ۸۱ کد تازهٔ `AV81` صادر می‌شود.
- ابزار صدور خصوصی مالک **در این مخزن عمومی نیست** (بخش `private/` در `.gitignore` است).
  برای ساخت ابزار خصوصی، راهنمای `docs/SECURITY-fa.md` را بخوانید.
- قیمت‌ها و متن «نحوهٔ خرید» بدون تغییر از نسخهٔ ۸۰ حفظ شده‌اند مگر اینکه مالک تغییر دهد.

## ساخت محلی / CI

- HTML: بدون بیلد؛ کافی است فایل را در مرورگر باز کنید.
- APK و EXE فقط در GitHub Actions ساخته می‌شوند (SDK/رانر لازم است).
- برای فعال‌سازی Pages: در GitHub به `Settings → Pages` بروید و Source را
  `GitHub Actions` بگذارید؛ workflow ‏`pages.yml`‏ منتشر می‌کند.

## مستندات

- `docs/SETUP-fa.md` — راه‌اندازی و ساخت
- `docs/MIGRATION-fa.md` — مهاجرت داده از ۱۳/۸۰ به ۸۱
- `docs/SECURITY-fa.md` — امنیت، کلیدها و امضا
- `docs/BUILD-81-fa.md` — گزارش ساخت نسخهٔ ۸۱ و محدودیت‌ها

## هش‌ها

پس از ساخت، فایل `SHA256SUMS-81.0.0.0` در Release منتشر می‌شود.
قبل از اجرا، هش فایل را بررسی کنید.
