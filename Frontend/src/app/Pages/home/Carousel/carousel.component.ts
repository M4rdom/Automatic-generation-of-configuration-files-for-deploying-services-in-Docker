import { Component } from '@angular/core';

import { MatButtonModule } from '@angular/material/button';
import { CarouselModule } from 'ngx-carousel-ease';

import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-carousel',
  standalone: true,
  imports: [
    MatCardModule,
    MatButtonModule,
    CarouselModule
  ],
  templateUrl: './carousel.component.html',
  styleUrl: './carousel.component.css'
})
export class CarouselComponent {
  constructor(
  ) {

  }

  ngAfterViewInit() {
    const previousButton = document.querySelector('button[aria-label="previous button navigation"]');
    
    (previousButton as HTMLElement).style.visibility = 'hidden';
    
    const nextButton = document.querySelector('button[aria-label="next button navigation"]');
    
    (nextButton as HTMLElement).style.visibility = 'hidden';
  }


  clickPreviousButton() {
    const previousButton = document.querySelector('button[aria-label="previous button navigation"]');
    if (previousButton) {
      (previousButton as HTMLElement).click();
    }
  }

  clickNextButton() {
    const nextButton = document.querySelector('button[aria-label="next button navigation"]');
    if (nextButton) {
      (nextButton as HTMLElement).click();
    }
  }
  
}
