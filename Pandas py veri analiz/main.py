import pandas as pd

# Örnek veri setini oluşturalım
veri = {
    'Ad': ['Ali', 'Veli', 'Ayşe', 'Fatma', 'Mehmet'],
    'Yaş': [25, 30, 35, 40, 45],
    'Cinsiyet': ['Erkek', 'Erkek', 'Kadın', 'Kadın', 'Erkek'],
    'Maaş': [5000, 6000, 5500, 7000, 8000]
}

# Veri setini bir DataFrame'e dönüştürelim
veri_df = pd.DataFrame(veri)

# Veri setini ekrana yazdıralım
print("=== Veri Seti ===")
print(veri_df)
print()

# Ortalama maaşı hesaplayalım
ortalama_maas = veri_df['Maaş'].mean()
print("Ortalama Maaş:", ortalama_maas)
print()

# En genç ve en yaşlı kişileri bulalım
en_genc = veri_df['Yaş'].min()
en_yasli = veri_df['Yaş'].max()
print("En genç kişi:", veri_df[veri_df['Yaş'] == en_genc]['Ad'].values[0])
print("En yaşlı kişi:", veri_df[veri_df['Yaş'] == en_yasli]['Ad'].values[0])
print()

# Cinsiyete göre gruplayalım ve ortalama maaşı hesaplayalım
cinsiyet_ortalamalari = veri_df.groupby('Cinsiyet')['Maaş'].mean()
print("Cinsiyete göre ortalama maaşlar:")
print(cinsiyet_ortalamalari)
