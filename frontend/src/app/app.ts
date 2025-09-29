import { Component, Inject, inject, signal } from '@angular/core';
import { RouterOutlet, RouterModule, Router } from '@angular/router';
import { CommonModule, AsyncPipe } from '@angular/common';
import { AuthService } from './services/auth';

@Component({
    selector: 'app-root',
    imports: [RouterOutlet, RouterModule, CommonModule, AsyncPipe],
    templateUrl: './app.html',
    styleUrl: './app.css'
})
export class App {
    protected readonly title = signal('frontend');
    auth = inject(AuthService);
    private router = Inject(Router);

    logout() {
        this.auth.logout();
        this.router.navigate(['/pojazdy'])
    }
}
