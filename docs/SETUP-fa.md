# راه‌اندازی و ساخت — AtaVision ۸۱

## پیش‌نیازها

- HTML: فقط یک مرورگر (بدون نصب).
- APK: GitHub Actions (Ubuntu + JDK 17 + Android SDK). ساخت محلی نیازمند Android Studio است.
- Windows: GitHub Actions (Windows + .NET 8 SDK + Inno Setup). ساخت محلی نیازمند .NET 8 و WebView2 Runtime است.

## فعال‌سازی GitHub Pages

1. در GitHub به `Settings → Pages` بروید.
2. Source را روی `GitHub Actions` بگذارید.
3. workflow ‏`pages.yml`‏ فایل `web/AtaVision-81.0.0.0-Offline.html` را به‌عنوان `index.html` و `web/version.json` را منتشر می‌کند.
4. نشانی سایت: `https://atapm2964-glitch.github.io/Ata/`

## ساخت خروجی‌ها

- با push تگ `v81.*` (مثلاً `v81.0.0.0`) workflow ‏`build-all.yml`‏ هر چهار خروجی را می‌سازد و Release منتشر می‌کند.
- ساخت دستی: در تب `Actions` روی `Build AtaVision 81` گزینهٔ `Run workflow` را بزنید؛ خروجی‌ها به‌صورت Artifact در دسترس‌اند.

## بررسی هش

پس از دانلود از Release:

```bash
sha256sum -c SHA256SUMS-81.0.0.0
```

در PowerShell:

```powershell
Get-FileHash .\نام-فایل -Algorithm SHA256
```

اگر هش متفاوت بود، فایل را اجرا نکنید.

## نکتهٔ مهم دربارهٔ امضای APK

APK ساخته‌شده در CI با گواهی debug امضا می‌شود. برای **ارتقای درجا** از نسخهٔ ۸۰،
گواهی باید دقیقاً همان گواهی نسخهٔ ۸۰ باشد؛ در غیر این صورت اندروید نصب درجا را رد می‌کند
و باید با پشتیبان JSON مهاجرت کنید. رجوع به `SECURITY-fa.md`.
