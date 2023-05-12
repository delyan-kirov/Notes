import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { SharedService } from "../shared.service"

@Component({
  selector: 'app-note-button',
  templateUrl: './note-button.component.html',
  styleUrls: ['./note-button.component.css'],
})

export class NoteButtonComponent
implements OnInit {
  constructor(private http: HttpClient) { }

  data : [string[], string[]] = [["1"], ["1"]];

  ngOnInit() {
    const url = "http://127.0.0.1:5000/init";
    this.http.get<[string[], string[]]>(url).subscribe(data => {
      console.log(data);
      this.data = data;
    });
  }

  openNote(index: string){

    const url = "http://127.0.0.1:5000/notes";
    const body = {name : index}
    console.log(body)
    this.http.post(url,body, {responseType: "text"}).subscribe();

    window.open(url, '_blank');
  }

  deleteElement(event: Event, item:string) {
    event.stopPropagation();
    console.log(item)
    const url = "http://127.0.0.1:5000/delete";
    const params = new HttpParams().set('filename', item);
    const options = { params: params };
    this.http.delete(url, options).subscribe(() => {
      console.log("refresh");
      this.ngOnInit();
    });
  }
}