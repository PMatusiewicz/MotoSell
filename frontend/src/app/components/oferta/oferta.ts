import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PojazdyService } from '../../services/pojazdy';
import { ActivatedRoute } from '@angular/router';
import { switchMap, Observable } from 'rxjs';

@Component({
    selector: 'app-oferta',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './oferta.html',
    styleUrl: './oferta.css'
})
export class OfertaComponent{
    private pojazdyService = inject(PojazdyService);
    private route = inject(ActivatedRoute);

    pojazd$: Observable<any> = this.route.paramMap.pipe(
        switchMap(params => {
            const id = params.get('id');
            if (id) {
                return this.pojazdyService.getOferta(id);
            } else {
                throw new Error('Brak ID pojazdu w URL');
            }
        })
    );
}
