import { Component, Input } from '@angular/core';
import { Project } from '../../project.model';

@Component({
  selector: 'project-details-info-card',
  templateUrl: './project-details-info-card.widget.html',
  styleUrls: ['./project-details-info-card.widget.css']
})
export class ProjectDetailsInfoCard {
  @Input() project: Project | undefined;

  constructor() {}
}
