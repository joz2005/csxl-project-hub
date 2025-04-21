import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'ai-search-bar',
  templateUrl: './ai-search-bar.widget.html',
  styleUrls: ['./ai-search-bar.widget.css']
})
export class AISearchBar {
  @Input() searchBarQuery: string = '';
  @Output() searchBarQueryChange = new EventEmitter<string>();

  constructor() {}

  onTextChanged() {
    this.searchBarQueryChange.emit(this.searchBarQuery);
  }
  clearSearch() {
    this.searchBarQuery = '';
    this.searchBarQueryChange.emit(this.searchBarQuery);
  }
}
