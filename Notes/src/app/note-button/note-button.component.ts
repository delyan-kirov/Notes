import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaderResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { SharedService } from "../shared.service"
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-note-button',
  templateUrl: './note-button.component.html',
  styleUrls: ['./note-button.component.css'],
})

export class NoteButtonComponent
implements OnInit {
  constructor(private route: ActivatedRoute, private http: HttpClient) {}

  data : [string[], string[]] = [["1"], ["1"]];

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      const username = params['username'];
      if (username) {
        const url = `http://localhost:5000/init?username=${username}`;
        this.http.get<[string[], string[]]>(url).subscribe(data => {
          console.log(data);
          this.data = data;
        });
      }
    });
  }

  openNote(index: string) {
    // const url = "http://192.168.0.15:5000/notes";
    const url = "http://localhost:5000/notes"
    const body = { name: index };
    console.log("posting a post request: " + body);
  
    const headers = new HttpHeaders({
      "Content-Type": "application/json",
      "Accept": "application/json"
    });
    this.http
      .post(url, body, { headers })
      .subscribe(response => {
        console.log("Got response." + response);
        const htmlContent = (response as any).content;
        const newWindow = window.open();
        if (newWindow) {
          newWindow.document.write(htmlContent);
        }
      });
  }
  
deleteElement(event: Event, item: string) {
    event.stopPropagation();
    console.log(item);
    
    this.route.queryParams.subscribe(params => {


      const username = params['username'];
      console.log("The username is: " + username)
      
      const url = `http://localhost:5000/delete?username=${username}`;
      const paramFile = new HttpParams().set('filename', item);
      const options = { params : paramFile };

      this.http.delete(url, options).subscribe(() => {
        console.log("refresh");
        this.ngOnInit();
      });
    })

}
}