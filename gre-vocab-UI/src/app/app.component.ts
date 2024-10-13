import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DictionaryService } from './dictionary.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  word: string = '';
  language: string = '';
  definition: string | undefined;

  constructor(private dictionaryService: DictionaryService) {}

  fetchDefinition(): void {
    this.dictionaryService.getTranslation(this.word, this.language).subscribe(
      data => {
        this.definition = data.definition; // Adjust based on your API response
      },
      error => {
        console.error('Error fetching definition:', error);
        this.definition = "Error fetching definition.";
      }
    );
  }
}
