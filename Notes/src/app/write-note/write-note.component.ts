import { Component, ViewChild, ElementRef  } from '@angular/core';
import { SharedService } from "../shared.service"


@Component({
  selector: 'app-write-note',
  templateUrl: './write-note.component.html',
  styleUrls: ['./write-note.component.css',
]
})

export class WriteNoteComponent {
  isComponentVisible = false;
  text = '';

  constructor(private sharedService: SharedService) {
    this.sharedService.isVisible$.subscribe(isVisible => {
      this.isComponentVisible = isVisible;
    });
  }
  @ViewChild('textInput') textInput!: ElementRef<HTMLTextAreaElement>;

  adjustHight(){
    const textArea = this.textInput.nativeElement;
    textArea.style.height = 'auto';
    textArea.style.height = textArea.scrollHeight + 'px';

    this.sharedService.setText(this.text);
  }

}
