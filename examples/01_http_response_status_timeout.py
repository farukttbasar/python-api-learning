import requests

r1 = requests.get('https://imgs.xkcd.com/comics/wirecutter_recommendation.png')

with open('comic.png', 'wb') as f:
    f.write(r1.content)

r2 = requests.get('https://xkcd.com/2693/')

print(r2) # çıktı -> object
#print(help(r2)) # Response modül yardım menüsü
print(r2.text) # html formatında yazıları döndürür
print(r2.status_code) # status codu döndürür, check etmek için kullanılır

"""

Durum Kodlarının 5 Ana Sınıfı

• 1xx (Bilgisel): İstek sunucuya ulaştı ve işlem devam ediyor.
• 2xx (Başarı): İstek sunucu tarafından başarıyla alındı, anlaşıldı ve onaylandı.
• 3xx (Yönlendirme): İsteğin tamamlanması için istemcinin (tarayıcının) ek bir işlem yapması (başka bir adrese gitmesi) gerekiyor.
• 4xx (İstemci Hatası): İstekte hata var veya istenen kaynak istemci tarafındaki bir sorundan dolayı bulunamıyor.
• 5xx (Sunucu Hatası): İstek geçerli olmasına rağmen sunucu kendi tarafındaki bir sorundan dolayı isteği yerine getiremiyor.

En Sık Karşılaşılan HTTP Durum Kodları

2xx: Başarı Kodları

• 200 OK (Tamam): İstek başarılı oldu ve talep edilen veri geri döndürüldü.
• 201 Created (Oluşturuldu): İstek başarılı oldu ve sunucuda yeni bir kaynak (veri) oluşturuldu.
• 204 No Content (İçerik Yok): İstek başarılı oldu ancak geri döndürülecek bir veri gövdesi yok.

3xx: Yönlendirme Kodları

• 301 Moved Permanently (Kalıcı Olarak Taşındı): İstenen sayfa veya kaynak kalıcı olarak yeni bir URL'e taşındı.
• 302 Found (Geçici Olarak Taşındı): Kaynak geçici olarak farklı bir URL'de bulunuyor.
• 304 Not Modified (Değiştirilmedi): İstenen kaynak son ziyaretten beri değişmedi, tarayıcı önbelleğindeki eski veri kullanılabilir.

4xx: İstemci (Kullanıcı) Hataları

• 400 Bad Request (Geçersiz İstek): Sunucu, hatalı sözdizimi nedeniyle isteği anlamadı veya işleyemedi.
• 401 Unauthorized (Yetkisiz): Kaynağa erişmek için kimlik doğrulaması (giriş yapılması) gerekiyor.
• 403 Forbidden (Yasaklandı): Sunucu isteği anladı ancak kullanıcının bu kaynağa erişim yetkisi yok.
• 404 Not Found (Bulunamadı): İstenen sayfa veya kaynak sunucuda bulunamadı (en sık karşılaşılan web hatasıdır).
• 429 Too Many Requests (Çok Fazla İstek): Kullanıcı belirli bir süre içinde sunucuya çok fazla istek gönderdi (hız sınırı).

5xx: Sunucu Hataları

• 500 Internal Server Error (İç Sunucu Hatası): Sunucuda beklenmedik bir hata oluştu ve istek tamamlanamadı.
• 502 Bad Gateway (Hatalı Ağ Geçidi): Sunucu, başka bir sunucudan geçersiz bir yanıt aldı.
• 503 Service Unavailable (Hizmet Kullanılamıyor): Sunucu şu anda aşırı yoğun veya bakımda olduğu için hizmet veremiyor.
• 504 Gateway Timeout (Ağ Geçidi Zaman Aşımı): Sunucu, arkadaki diğer sunucudan zamanında yanıt alamadı.

"""
print(r2.headers) # ilgili başlıkları döndürür, content type, last modified...

# TIMEOUT

r3 = requests.get('https://httpbin.org/delay/1', timeout=3) # [200]
r4 = requests.get('https://httpbin.org/delay/5', timeout=3) # timeout

print(r3)
print(r4)
