import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'ai-resume-search',
  templateUrl: './ai-resume-search.widget.html',
  styleUrls: ['./ai-resume-search.widget.css']
})
export class AiResumeSearch {
  public selectedFile: File | null = null;

  public get isValid(): boolean {
    return !!this.selectedFile
  }

  constructor(protected dialogRef: MatDialogRef<AiResumeSearch>) {}

  public onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
    }
  }

  public uploadResume(): void {
    if (this.isValid && this.selectedFile) {
      this.dialogRef.close(this.selectedFile);
    }
  }

  public close(): void {
    this.dialogRef.close();
  }
}