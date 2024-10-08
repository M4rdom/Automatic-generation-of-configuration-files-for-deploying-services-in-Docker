import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SidenavContentComponent } from './sidenav-content.component';

describe('SidenavContentComponent', () => {
  let component: SidenavContentComponent;
  let fixture: ComponentFixture<SidenavContentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SidenavContentComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SidenavContentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
