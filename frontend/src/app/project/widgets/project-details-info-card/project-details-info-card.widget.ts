import { Component, Input } from '@angular/core';
import { Project } from '../../project.model';

@Component({
  selector: 'project-details-info-card',
  templateUrl: './project-details-info-card.widget.html',
  styleUrls: ['./project-details-info-card.widget.css']
})
export class ProjectDetailsInfoCard {
  @Input() project: Project | undefined;

  showForm = false;

  formData = {
    name: '',
    email: '',
    message: ''
  };

  submitApplication() {
    console.log('Application submitted:', this.formData);

    // Reset form and hide it
    this.formData = {
      name: '',
      email: '',
      message: ''
    };
    this.showForm = false;
  }
  constructor() {}
}
