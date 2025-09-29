import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PojazdyService } from '../../services/pojazdy';
import { RouterModule } from '@angular/router';

@Component({
    selector: 'app-pojazdy',
    standalone: true,
    imports: [CommonModule, RouterModule],
    templateUrl: './pojazdy.html',
    styleUrl: './pojazdy.css'
})
export class PojazdyComponent {
    private pojazdService = inject(PojazdyService);
    pojazdy$ = this.pojazdService.getPojazdy();
}