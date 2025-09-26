import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Pojazdy } from './pojazdy';

describe('Pojazdy', () => {
  let component: Pojazdy;
  let fixture: ComponentFixture<Pojazdy>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Pojazdy]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Pojazdy);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
