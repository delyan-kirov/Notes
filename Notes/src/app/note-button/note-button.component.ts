import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { NgClass, NgFor } from '@angular/common';

@Component({
  selector: 'app-note-button',
  styleUrls: ['./note-button.component.css'],
  template: `
    <div *ngFor="let item of data[1]; let i = index">
    <button (click)="openNote(item)" class="my-button button1">
    <div class="button-part-1">
      <div class="name-field">{{item}}</div>
    </div>
    <div class="button-part-2">
      <div class="snippet-field">{{data[0][i]}}</div>
    </div>
</button>
    </div>
  `
})
export class NoteButtonComponent
implements OnInit {
  constructor(private http: HttpClient) { }

  data : [string[], string[]] = [["1"], ["1"]];

  ngOnInit() {
    // this.getData();
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
    this.http.post(url,body).subscribe();

    window.open(url, '_blank');
  }

}