import { Component } from '@angular/core';
import { SharedService } from "../shared.service"

@Component({
  selector: 'app-button-container',
  templateUrl: './button-container.component.html',
  styleUrls: ['./button-container.component.css']
})
export class ButtonContainerComponent{
  isComponentVisible = true;
  
  constructor(private sharedService: SharedService) {
    this.sharedService.isVisible$.subscribe(isVisible => {
      this.isComponentVisible = !isVisible;
    });
  }
}