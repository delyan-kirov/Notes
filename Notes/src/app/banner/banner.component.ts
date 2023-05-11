import { Component } from '@angular/core';
import { SharedService } from "../shared.service"

@Component({
  selector: 'app-banner',
  templateUrl: './banner.component.html',
  styleUrls: ['./banner.component.css']
})

export class BannerComponent {
  
    login() {
      // Add your login logic here
    }
  
    register() {
      // Add your register logic here
    }

    constructor(private sharedService: SharedService) {}

    isComponentVisible = false;

    toggleComponent() {
      console.log("Component is not visible? " + this.isComponentVisible);
      this.isComponentVisible = !this.isComponentVisible;

      this.sharedService.updateVisibility(this.isComponentVisible);
    }
  
    // Add other central command methods here
}
