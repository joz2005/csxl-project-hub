import { Component, Input } from '@angular/core';
import { Project } from '../../project.model';
import { Profile } from '../../../profile/profile.service';

@Component({
  selector: 'project-card',
  templateUrl: './project-card.widget.html',
  styleUrls: ['./project-card.widget.css']
})
export class ProjectCard {
  @Input() project!: Project;
  constructor() {}
}
