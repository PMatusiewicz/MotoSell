import { TestBed } from '@angular/core/testing';

import { PojazdyService } from './pojazdy';

describe('Pojazdy', () => {
  let service: PojazdyService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PojazdyService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
