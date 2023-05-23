import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class SharedService {


  private _isVisible = new BehaviorSubject<boolean>(false);
  public isVisible$ = this._isVisible.asObservable();

  updateVisibility(isVisible: boolean) {
    this._isVisible.next(isVisible);
  }

  // //////////////////////////////////////////////////////

  private text: string = "";

  private _text = new BehaviorSubject<string>("");
  public text$ = this._text.asObservable();

  setText(text: string) {
    console.log("setting text");
    this._text.next(text);
}

  getText() {
    console.log("getting text");
    console.log(this.text);
    return this.text$
  }

  constructor() { }
}


