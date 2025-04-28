import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Project } from '../../project.model';
import { Profile } from '../../../profile/profile.service';

@Component({
  selector: 'project-card',
  templateUrl: './project-card.widget.html',
  styleUrls: ['./project-card.widget.css']
})
export class ProjectCard {
  @Input() project!: Project;
  @Input() profile!: Profile;
  @Output() deleteProject = new EventEmitter<number>();

  canDelete(): boolean {
    return this.profile.id === this.project.author_id;
  }

  onDelete() {
    this.deleteProject.emit(this.project.id!);
  }
}
