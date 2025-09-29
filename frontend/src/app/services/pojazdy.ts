import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Uzytkownik {
    username: string;
}

interface Zdjecia {
    zdjecie: string;
    czy_glowny: boolean;
}

interface Pojazd {
    id: number;
    tytul: string;
    opis: string;
    kategoria: string;
    marka: string;
    model: string;
    rok_produkcji: number;
    przebieg: number;
    pojemnosc_skokowa: number;
    rodzaj_paliwa: string;
    czy_opublikowany: boolean;
    uzytkownik: Uzytkownik;
    zdjecia: Zdjecia[];
}

@Injectable({
    providedIn: 'root'
})
export class PojazdyService {
    private http = inject(HttpClient);
    private apiUrl = 'http://localhost:8000/api/pojazdy/';
    getPojazdy(): Observable<Pojazd[]> {
        return this.http.get<Pojazd[]>(this.apiUrl);
    }
    getOferta(id: string | number): Observable<Pojazd> {
        return this.http.get<Pojazd>(`${this.apiUrl}${id}/`);
    }
}
