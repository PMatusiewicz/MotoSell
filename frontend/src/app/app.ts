import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Pojazdy } from './components/pojazdy/pojazdy';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Pojazdy],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {
  protected readonly title = signal('frontend');
}
