
D={'a':0,'b':1,'c':2}
print (D)
print (D['a'])
print (D.keys())
print (D.values())

# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print (release_year_dict)

release_year_dict['Thriller'] # 1982

# Append value with key into dictionary

release_year_dict['Graduation'] = '2007' 
print (release_year_dict)

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print (release_year_dict)


Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
#What is the result of the following operation: Dict["D"]?

print (Dict["D"])

# 
poblacion_paises = {
    "Argentina": 450_200_300,
    "Mexico": 320_200_300,
    "Brasil": 950_200_300,

}


for pais in poblacion_paises.values():
    print (pais)

for pais in poblacion_paises.keys():
    print (pais)

for pais, poblacion in poblacion_paises.items():
    print (pais + ' tiene ' + str(poblacion) + ' habitantes')

