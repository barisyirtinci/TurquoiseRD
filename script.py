import sys

if len(sys.argv) != 4:
    print("Kullanım: script.py <city> <country> <year>")
    sys.exit(1)

city = sys.argv[1]
country = sys.argv[2]
year = sys.argv[3]

#print(f"Seçilen şehir: {city}")
#print(f"Seçilen ülke: {country}")
#print(f"Seçilen yıl: {year}")

if(country == "Turkey"):
    print(51.4,66.5)
else:
    print(41.9,36.8)


# Burada Python kodunuzun gerçek işlemini yapabilirsiniz.
# Örneğin, bu verileri kullanarak bir veritabanı sorgusu yapabilir veya bir analiz gerçekleştirebilirsiniz.

