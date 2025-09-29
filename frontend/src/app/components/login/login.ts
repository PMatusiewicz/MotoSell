import { Component } from '@angular/core';
import { AuthService } from '../../services/auth';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-login',
    imports: [FormsModule],
    templateUrl: './login.html',
    styleUrl: './login.css'
})
export class LoginComponent {
    username = '';
    password = '';
    error = '';

    constructor(private auth: AuthService, private router: Router) {}

    login() {
        this.auth.login(this.username, this.password).subscribe({
        next: () => this.router.navigate(['/']),
        error: err => this.error = 'Błędne dane logowania'
        });
    }
}
