import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { tap } from 'rxjs/operators';

interface LoginResponse {
    access: string;
    refresh: string;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
    private http = inject(HttpClient);
    private apiUrl = 'http://localhost:8000/api/token/';

    private loggedIn = new BehaviorSubject<boolean>(!!localStorage.getItem('access_token'));
    isLoggedIn$ = this.loggedIn.asObservable();

    login(username: string, password: string): Observable<LoginResponse> {
        return this.http.post<LoginResponse>(this.apiUrl, { username, password }).pipe(
        tap((res) => {
            localStorage.setItem('access_token', res.access);
            localStorage.setItem('refresh_token', res.refresh);
            this.loggedIn.next(true);
        })
        );
    }

    logout() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        this.loggedIn.next(false);
    }

    getToken() {
        return localStorage.getItem('access_token');
    }
}