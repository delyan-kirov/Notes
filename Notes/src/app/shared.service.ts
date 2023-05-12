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

  setText(text: string) {
    console.log("setting text");
    this.text = text;
  }
  
  getText() {
    console.log("getting text");
    return this.text;
  }

  constructor() { }
}
