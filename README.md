# Projekts
Projektā tiek izmantoti divi faili (excel un csv). Excel failā doti dati par dažādām personām (Atrašanās vieta, vārds, uzvārds, vecums un dzimums).
CSV failā ir ASV pilsētu nosaukumi un atbilstošie zip kodi. Programmas uzdevums ir uzzināt terminālī ievadītās pilsētas zip kodu, aprēķināt cik
personas (excel failā) ir no šīs vietas un balstoties uz excel faila dotot informāciju, aprēķināt kāds ir vidējais vecums personām no norādītās
pilsētas.
CSV fails tika iegūts no oficiālas mājaslapas, kur tiek dota detalizēta informācija par dažādām vietām ASV. Excel fails ir datora ģenerēts, kas
nozīmē, ka visi dati ir bijuši nejauši ģenerēti. Lai pārbaudītu vai programma strādā, izmantoju "Arvada" pilsētu, jo no šīs pilsētas excel failā
ir 3 personas.
Projektam izmantoju pandas bibliotēku, jo iepriekšēji strādājot ar šo bibliotēku laboratorijas darbos, nesaskāros ar lieliem šķēršļiem. Kā arī
man šī bibliotēka likās piemērota, jo darbs tika veikts apvienojot informāciju no Excel un CSV failiem.
Šāda programma var būt noderīga ikvienam, kam jāstrādā, piemēram, ar klientu datubāzi, konkrēti ar klientu atrašanās vietām. Šāda datubāze var
tikt imantota firmās, kurās viens no uzdevumiem ir preču piegāde. Firmai ir iespējams apkopot informāciju, kāds klientu skaits un vidējais vecums
ir no katras pilsētas, kā arī uzreiz noskaidrot pilsētas zip kodus.
