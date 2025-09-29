import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PojazdyComponent } from './pojazdy';

describe('Pojazdy', () => {
    let component: PojazdyComponent;
    let fixture: ComponentFixture<PojazdyComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
        imports: [PojazdyComponent]
        })
        .compileComponents();

        fixture = TestBed.createComponent(PojazdyComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
