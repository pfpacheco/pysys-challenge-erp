import { Injectable } from '@angular/core';

import {Observable, throwError} from 'rxjs';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';

import { Person } from './interfaces/person';
import {catchError, retry} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {

  private baseUrl = 'http://localhost:5000/api';

  constructor(
    private httpClient: HttpClient
  ) { }

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    })
  };

  public addPerson(person: Person): Observable<{}> {
    const url = this.baseUrl + '/person/addPerson';
    const payload = { person: JSON.stringify(person)};
    const response: Observable<any> = this.httpClient.post(url, payload, this.httpOptions);
    return response.pipe(
      retry(1),
      catchError(this.handleError)
      );
  }

  handleError(error: HttpErrorResponse) {
    let errorMessage;
    if (error.error instanceof ErrorEvent) {
      errorMessage = error.error.message;
    } else {
      errorMessage = 'Error code: ${error.status}, ' + 'message: ${error.message}';
    }
    console.log('errorMessage: ' + errorMessage);
    return throwError(errorMessage);
  }
}
