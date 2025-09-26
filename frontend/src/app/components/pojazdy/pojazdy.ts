import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PojazdyService } from '../../services/pojazdy';

@Component({
  selector: 'app-pojazdy',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './pojazdy.html',
  styleUrl: './pojazdy.css'
})
export class Pojazdy implements OnInit {
  pojazdy: any[] = [];
  private pojazdService = inject(PojazdyService);

  ngOnInit(): void {
  this.pojazdService.getPojazdy().subscribe({
    next: data => {
      console.log('Dane z API:', data); // sprawdź w konsoli po odświeżeniu
      this.pojazdy = data;
    },
    error: err => {
      console.error('Błąd pobierania:', err);
    }
  });
}
}
