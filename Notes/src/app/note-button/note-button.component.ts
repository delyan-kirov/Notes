import { Component } from '@angular/core';

@Component({
  selector: 'app-note-button',
  templateUrl: './note-button.component.html',
  styleUrls: ['./note-button.component.css']
})
export class NoteButtonComponent {
  openNote(){
    alert("The button is clicked!")
  }
}

