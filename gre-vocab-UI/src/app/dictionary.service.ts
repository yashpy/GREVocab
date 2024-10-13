import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DictionaryService {
  private apiUrl = 'http://127.0.0.1:3000/analyze';

  constructor(private http: HttpClient) {}

  getTranslation(language: string, word: string): Observable<any> {
    return this.http.post<any>('http://127.0.0.1:3000/translate', {
      language: language,
      input_word: word
    });
  }
}