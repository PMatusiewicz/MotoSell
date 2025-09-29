import { Routes } from '@angular/router';
import { PojazdyComponent } from './components/pojazdy/pojazdy';
import { OfertaComponent } from './components/oferta/oferta';
import { LoginComponent } from './components/login/login';

export const routes: Routes = [
    { path: '', redirectTo: 'pojazdy', pathMatch: 'full'},
    { path: 'pojazdy', component: PojazdyComponent },
    { path: 'pojazdy/:id', component: OfertaComponent},
    { path: 'login', component: LoginComponent}
];
