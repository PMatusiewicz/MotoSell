import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Pojazd {
  tytul: string;
  opis: string;
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
}
