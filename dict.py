meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap" ,
            "SHEESH": "onaylamamak" ,
            "ROYALPLAY": "rol yapma" ,
            "DOKİ DOKİ": "kalp atışı" ,
            "CREEPY": "korkunç" ,
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
            
kelime= input("Anlamadığınız bir kelime yazın(hepsini büyük harflerle yazın)")

if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print("bu kelime sözlükte yok")
