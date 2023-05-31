import { Component } from '@angular/core';
import { SharedService } from "../shared.service"
import { HttpClient } from '@angular/common/http';
import { take } from 'rxjs/operators';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-banner',
  templateUrl: './banner.component.html',
  styleUrls: ['./banner.component.css']
})

export class BannerComponent {


  constructor(
    private sharedService: SharedService,
    private http: HttpClient,
    private route: ActivatedRoute
) {}

    isComponentVisible = false;
    isButtonVisible = false;

    toggleComponent() {
      console.log("Component is not visible? " + this.isComponentVisible);
      this.isComponentVisible = !this.isComponentVisible;
      this.isButtonVisible = !this.isButtonVisible;
      this.sharedService.updateVisibility(this.isComponentVisible);
    }
    
    sendText() {

      this.route.queryParams.subscribe(params => {
        const username = params['username'];
        if (username) {
          console.log("This is the username: " + username);
          this.sharedService.getText().pipe(take(1)).subscribe(text => {
            console.log("I subscribed and got: " + text);
            // const url = "http://192.168.0.15:5000/text"
            const url = `http://localhost:5000/text?username=${username}`
            this.http.post(url, { text }).subscribe(response => {
            });
          });
        }
      });

    }

    clearField(){
      console.log("Clearing the field.");
      this.sharedService.setText("");
    }
  

}
