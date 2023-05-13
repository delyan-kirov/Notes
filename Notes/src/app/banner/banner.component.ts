import { Component } from '@angular/core';
import { SharedService } from "../shared.service"
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-banner',
  templateUrl: './banner.component.html',
  styleUrls: ['./banner.component.css']
})

export class BannerComponent {


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
      this.http.post('http://192.168.0.15:5000/text', { text }).subscribe(response => {
      });
    }
  

}
