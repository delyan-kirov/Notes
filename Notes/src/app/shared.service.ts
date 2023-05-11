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
  constructor() { }
}
