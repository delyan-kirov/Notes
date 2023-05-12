import { Component } from '@angular/core';
import { SharedService } from "../shared.service"
import { HttpClient } from '@angular/common/http';

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

    constructor(private sharedService: SharedService, private http: HttpClient) {}

    isComponentVisible = false;

    toggleComponent() {
      console.log("Component is not visible? " + this.isComponentVisible);
      this.isComponentVisible = !this.isComponentVisible;

      this.sharedService.updateVisibility(this.isComponentVisible);
    }

    sendText() {
      const text = this.sharedService.getText();
      console.log(text);
      this.http.post('http://127.0.0.1:5000/text', { text }).subscribe(response => {
        // handle the response here
      });
    }
  
    // Add other central command methods here
}
