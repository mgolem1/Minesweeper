# Minesweaper

Minesweeper je puzzle video igra za jednog igrača. Cilj igre je očistiti pravokutnu ploču koja sadrži skrivene "mine" ili bombe bez detoniranja bilo koje od njih, uz pomoć tragova o broju susjednih mina u svakom polju. 

Igrači mogu odlučiti ponoviti ploču u kojoj se igra otkrivanjem kvadrata mreže klikom ili označavanjem svakog kvadrata na bilo koji drugi način. Ako se otkrije kvadrat koji sadrži minu, igrač gubi igru. Ako se ne otkrije nikakva mina, umjesto toga na kvadratu se prikazuje znamenka koja označava koliko susjednih kvadrata sadrži mine; ako nijedna mina nije susjedna, kvadrat postaje prazan i svi će se susjedni kvadrati rekurzivno otkriti. Igrač koristi ove podatke za utvrđivanje sadržaja drugih kvadrata i može sigurno otkriti svaki kvadrat ili označiti kvadrat kao da sadrži minu.

U Minolovcu su mine razasute po ploči koja je podijeljena u stanice. Stanice imaju tri stanja: nepokrivene, pokrivene i označene. Prekrivena ćelija je prazna i na nju se može kliknuti, dok je nepokrivena ćelija izložena. Označene stanice su one koje je igrač označio kako bi ukazao na potencijalno mjesto mina.

Ako igrač otkrije miniranu ćeliju, igra završava, jer postoji samo 1 život po utakmici. Inače, nepokrivene ćelije prikazuju broj, koji označava količinu mina uz nju, ili praznu pločicu (ili "0"), a sve susjedne neminirane stanice automatski će se otkriti. Desni klik na ćeliju označit će je zastavicom, zbog čega će se na njoj pojaviti zastavica. Označene ćelije i dalje se smatraju prekrivenima, a igrač ih može kliknuti kako bi ih otkrio, iako ih obično prvo treba ukloniti dodatnim desnim klikom.

Prvi klik u bilo kojoj igri nikada neće biti rudnik.

Da bi pobijedili u igri, igrači moraju otkriti sve stanice koje nisu mine, a u tom se trenutku tajmer zaustavlja. Označavanje svih miniranih stanica nije potrebno.
